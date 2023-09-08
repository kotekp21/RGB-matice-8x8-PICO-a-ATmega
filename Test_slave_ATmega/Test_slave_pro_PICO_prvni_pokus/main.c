/*
 * Test_slave_pro_PICO_prvni_pokus.c
 *
 * Created: 19.07.2023 17:15:29
 * Author : kotekp21
 */ 

/* I2C Echo Example */
#ifndef F_CPU
#define F_CPU 16000000UL
#endif

#include "I2CSlave.h"
#include <util/delay.h>
#include <avr/io.h>
#include <util/delay.h>

#define I2C_ADDR 0x10

volatile uint8_t data;

// PB0 -> Clock
// PB1 -> Clear
// PB2 -> AB registru (nejbli��� k matici)
// PB3 -> AB registru (prost�edn�)
// PB4 -> AB registru (nejvzd�len�j�� od matice)
// PD0 - PD7 -> ��dky 1 - 8
// PC4 -> I2C SDA (zelen�)
// PC5 -> I2C CLK (b�l�)

// ! NESAHAT NA: !
// PC6 - Reset
// PB3 - MOSI komunikace
// PB4 - MISO komunikace
// PB5 - SCK hodiny komunikace

// VRCHN� STRANA MATICE JE U NAP�JEN� NA NEP�JKU

//         y  x  barva
int Buffer[8][8][3];
int VstupyRegistru[] = {PORTB4, PORTB3, PORTB2};
int Radky[] = {PORTD0, PORTD1, PORTD2, PORTD3, PORTD4, PORTD5, PORTD6, PORTD7};
int HodinyRegistru = PORTB0;
int ClearRegistru = PORTB1;
int Ledka = PORTB5;
int CisloBarvy = 1;
// CisloBarvy je pomocn� prom�nn� pro sah�n� do bufferu - HODNOTA 1 JE NASTAVENA KV�LI ZVL��TN�MU (nev�m co ho zp�sobuje) POSUNU
// 0 -> �erven�, 1 -> Zelen�, 2 -> Modr�
int CisloSloupce = 5;
// CisloSloupce je pomocn� prom�nn� pro sah�n� do bufferu - OP�T HODNOTA JIN� NE� NULA, PROTO�E DIVN� POSUN
int KontinuitaRegistru = 0;
// By� tato prom�nn� zn� ��len�, slou�� k ur�en�, kdy m� kter� registr na vstup nastavit 0 -> rozsv�cen�
int Pocitadlo_prijmu_radky = 0;
int Pocitadlo_prijmu_barvy = 0;
int Rezim = 1;

void I2C_received(uint8_t received_data)
{
	data = received_data;
		
	if (Rezim == 0)
	{
		for(int i = 0; i < 8; i++){
			Buffer[Pocitadlo_prijmu_radky][i][0] = (data >> i) & 1;
		}
		Pocitadlo_prijmu_radky++;
		if (Pocitadlo_prijmu_radky == 8) Pocitadlo_prijmu_radky = 0;
	}
	else if (Rezim == 1){
		for(int i = 0; i < 8; i++){
			Buffer[Pocitadlo_prijmu_radky][i][Pocitadlo_prijmu_barvy] = (data >> i) & 1;
		}
		Pocitadlo_prijmu_barvy++;
		if (Pocitadlo_prijmu_barvy == 3){
			Pocitadlo_prijmu_barvy = 0;
			Pocitadlo_prijmu_radky++;
			if (Pocitadlo_prijmu_radky == 8) Pocitadlo_prijmu_radky = 0;
		}
	}
}

void I2C_requested()
{
	//I2C_transmitByte(data);
}

void InicializaceRegistru()
{
	// Vyclearov�n� v�ech registr� p�i nov�m zapnut�
	for(int i = 0; i < 8; i++)
	{
		PORTD |= 1 << Radky[i];
	}

	PORTB &= 255 - (1 << ClearRegistru);
	PORTB |= 1 << ClearRegistru;

	// Zhasnut� v�eho (na stran� registr�)
	for(int i = 0; i < 3; i++)
	{
		PORTB |= 1 << VstupyRegistru[i];
	}

	for(int i = 0; i < 8; i++)
	{
		PORTB |= 1 << HodinyRegistru;
		PORTB &= 255 - (1 << HodinyRegistru);
	}
	
	/*
	PORTC &= 255 - (1 << VstupyRegistru[0]);
	PORTC |= 1 << HodinyRegistru;
	PORTC &= 255 - (1 << HodinyRegistru);
	PORTC|= 1 << VstupyRegistru[0];
	*/
}

void VynulovaniBufferu()
{
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			for (int k = 0; k < 3; k++)
			{
				Buffer[i][j][k] = 0;
			}
		}
	}
}

void PosunRegistru()
{
	// Do registr� se po�le 0 (rozsv�cen�) je-li spr�v� chv�le
	if (KontinuitaRegistru == 7)
	{
		PORTB &= 255 - (1 << VstupyRegistru[0]);
	}
	else if (KontinuitaRegistru == 15)
	{
		PORTB &= 255 - (1 << VstupyRegistru[1]);
	}
	else if (KontinuitaRegistru == 23)
	{
		PORTB &= 255 - (1 << VstupyRegistru[2]);
	}
	
	// Hodiny posunou registr
	PORTB |= 1 << HodinyRegistru;
	PORTB &= 255 - (1 << HodinyRegistru);
	
	// P��padn� 0 pos�lan� do registr� se zase zahsnout (po�le se 1)
	for (int i = 0; i < 3; i++)
	{
		PORTB |= 1 << VstupyRegistru[i];
	}

	// Zm�na hodnot pomocn�ch prom�nn�ch pro buffer a KontinuituRegistru
	KontinuitaRegistru += 1;
	if (KontinuitaRegistru == 24)
	{
		KontinuitaRegistru = 0;
	}
	CisloBarvy += 1;
	if (CisloBarvy == 3)
	{
		CisloBarvy = 0;
		CisloSloupce += 1;
		if (CisloSloupce == 8)
		{
			CisloSloupce = 0;
		}
	}
}

void ZhasnutiRadku()
{
	for (int i = 0; i < 8; i++)
	{
		PORTD &= 255 - (1 << Radky[i]);
	}
}

void RozsviceniRadkuDleBufferu()
{
	for (int i = 0; i < 8; i++)
	{
		if (Buffer[i][CisloSloupce][CisloBarvy])
		{
			PORTD |= 1 << Radky[i];
		}
		else
		{
			PORTD &= 255 - (1 << Radky[i]);
		}
	}
}

void setup()
{
	// set received/requested callbacks
	I2C_setCallbacks(I2C_received, I2C_requested);

	// init I2C
	I2C_init(I2C_ADDR);
	
	DDRB = 0xFF;
	DDRC = 0x00;
	DDRD = 0b11111111;
	
	PORTC |= (1 << PINC4);
	PORTC |= (1 << PINC5);
}

int main()
{
	setup();
	InicializaceRegistru();
	VynulovaniBufferu();
	Buffer[0][0][0] = 1;
	while (1)
	{
		cli();
		ZhasnutiRadku();
		PosunRegistru();
		RozsviceniRadkuDleBufferu();
		sei();
	}
	// Main pro
}

