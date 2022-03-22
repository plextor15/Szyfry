#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const int ile = 36;
const char alph[ile] = { 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U', 'V', 'W', 'X', 'Y', 'Z',
						'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

int main()
{
	ofstream zaszyfrowany;
	ofstream odszyfrowany;
	ifstream niezaszyfrowany;
	ifstream zaszyfrowany2;

	int przesuniecie = 0;
	bool co_robic = true; //true-szyfrowanie, false-odszyfrowanie
	bool koniec_pliku = false;

	char tmp_char;
	string tmp_str = "";
	int tmp_int;

	//zaszyfrowany.open("zaszyfrowany.txt");
	//odszyfrowany.open("odszyfrowany.txt");
	//niezaszyfrowany.open("niezaszyfrowany.txt");
	//zaszyfrowany2.open("zaszyfrowany.txt");

	std::cout << "Szyfrowanie [s], czy deszyfrowanie [d]?: ";
	std::cin >> tmp_char;
	if (tmp_char == 's')
	{
		co_robic = true;
	}
	if (tmp_char == 'd')
	{
		co_robic = false;
	}

	std::cout << "Podaj przesuniecie: ";
	std::cin >> przesuniecie;

	if (co_robic)
	{
/*
*	SZYFROWANIE
*/
		zaszyfrowany.open("zaszyfrowany.txt");
		niezaszyfrowany.open("niezaszyfrowany.txt");

		while (!koniec_pliku)
		{
			//if (niezaszyfrowany.eof())
			//{
			//	koniec_pliku = true;
			//	std::cout << "X"; //DEBUG ONLY!!
			//	//break;
			//	//zaszyfrowany.close();
			//	goto koniec;
			//}

			niezaszyfrowany >> std::noskipws >> tmp_char;
				if (niezaszyfrowany.eof()) goto koniec;
			//std::cout << tmp_char << " ----> "; //DEBUG ONLY!!

			if (((int)tmp_char >= 48 && (int)tmp_char <= 57) ||
				((int)tmp_char >= 65 && (int)tmp_char <= 90) ||
				((int)tmp_char >= 97 && (int)tmp_char <= 122))
			{
				//to mozna szyfrowac/deszyfrowac
				if ( (int)tmp_char >= 97 && (int)tmp_char <= 122 )
				{
					tmp_char = toupper( (int)tmp_char );
				}

				for (size_t i = 0; i < ile; i++)
				{
					if (tmp_char == alph[i])
					{
						i += przesuniecie;
						tmp_int = i % ile;

						zaszyfrowany << alph[tmp_int];
						//zaszyfrowany.flush();
						//tmp_str += alph[tmp_int];
						//std::cout << alph[tmp_int] << "\n"; //DEBUG ONLY!!
						break;
					}
				}
			}
			else
			{
				//przechodzi jak w oryginale
				zaszyfrowany << std::noskipws << tmp_char;
				zaszyfrowany.flush();
				//tmp_str += tmp_char;
				//std::cout << "--\n"; //DEBUG ONLY!!
			}
		}
koniec:
		zaszyfrowany.close();
		niezaszyfrowany.close();
	}
/*
*	ODSZYFROWYWANIE
*/
	else
	{
		odszyfrowany.open("odszyfrowany.txt");
		zaszyfrowany2.open("zaszyfrowany.txt");

		while (!koniec_pliku)
		{
			//std::cout << " + \n"; //DEBUG ONLY!!
			//if (zaszyfrowany2.eof())
			//{
			//	koniec_pliku = true;
			//	//break;
			//	goto koniec2;
			//}

			zaszyfrowany2 >> std::noskipws >> tmp_char;
				if (zaszyfrowany2.eof()) goto koniec;
			//std::cout << tmp_char << " ----> "; //DEBUG ONLY!!

			if (((int)tmp_char >= 48 && (int)tmp_char <= 57) ||
				((int)tmp_char >= 65 && (int)tmp_char <= 90))
			{
				//to mozna szyfrowac/deszyfrowac
				//if ((int)tmp_char >= 97 && (int)tmp_char <= 122)
				//{
				//	tmp_char = toupper((int)tmp_char);
				//}

				for (size_t i = 0; i < ile; i++)
				{
					if (tmp_char == alph[i])
					{
						i += ile - przesuniecie;
						tmp_int = i % ile;

						odszyfrowany << alph[tmp_int];
						//tmp_str += alph[tmp_int];
						//std::cout << tmp_int << " - " << alph[tmp_int] << "\n"; //DEBUG ONLY!!
					}
				}
			}
			else
			{
				//przechodzi jak w oryginale
				odszyfrowany << std::noskipws << tmp_char;
				//tmp_str += tmp_char;
				//std::cout << "--\n"; //DEBUG ONLY!!
			}
		}
koniec2:
		odszyfrowany.close();
		zaszyfrowany2.close();
	}

//koniec: //od goto
	/*for (size_t i = 0; i < tmp_str.size()-1; i++)
	{
		zaszyfrowany << std::noskipws << tmp_str[i];
	}*/
	

	//zaszyfrowany.close();
	//niezaszyfrowany.close();

	//zaszyfrowany.close();
	//niezaszyfrowany.close();
	
	return 0;
}