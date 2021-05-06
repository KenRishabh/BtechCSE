#include<stdio.h>
#include<conio.h>
int main()
{

     int r;
     float volume_sphere;
     clrscr();
     printf("Enter Radius : ");
     scanf("%d",&r);
     volume_sphere = (4/3.0)*3.14*r*r*r;
     printf("\nVolume of Sphere = %f",volume_sphere);
     getch();
     return 0;

}