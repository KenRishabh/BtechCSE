#include<stdio.h>
#include<conio.h>
int main()
{
	float vol,r,h;
	clrscr();
	printf("enter radius: ");
	scanf("%f",&r);
	printf("enter height: ");
	scanf("%f",&h);
	vol=(22*r*r*h)/7;
	printf("Volume Of Cylinder: %f\n",vol);
	getch();
	return 0;
}