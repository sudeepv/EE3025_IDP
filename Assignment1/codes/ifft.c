#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <string.h>


/*IFFT computed in a way similar to fft*/
void ifft(double complex* x, int n){
    
    /*Base case*/
    if (n == 1)
        return;

	/*Dividing the inverse DFT into it's even and odd parts*/
    double complex* odd = malloc(n/2 * sizeof(double complex));
    double complex* even = malloc(n/2 * sizeof(double complex));
    for (int i = 0; 2 * i < n; i++) {
        even[i] = x[2 * i];
        odd[i] = x[2 * i + 1];
    }

    /*Recursive calls to even and odd parts of DFT*/
    ifft(even, n/2);
    ifft(odd, n/2);

    /*Merging the even and odd parts of DFT*/
    double complex w;
    for (int i = 0; 2 * i < n; i++) {
        w = CMPLX(cos(-2*M_PI*i/n), sin(-2*M_PI*i/n));
        x[i] = even[i] + w * odd[i];
        x[i + n/2] = even[i] - w * odd[i];
    }

    /*Free memory*/
    free(even);
    free(odd);
}

int main()
{
    int n= (1<<20);
    
    double complex* X = (double complex*)malloc(n * sizeof(double complex));
    double complex* H = (double complex*)malloc(n * sizeof(double complex));
    double complex* Y = (double complex*)malloc(n * sizeof(double complex));
    double complex* ifft_Y = (double complex*)malloc(n * sizeof(double complex));
    
    FILE *fin1,*fin2,*fout1;

    /*Reading fft_x.dat*/
    fin1 = fopen("fft_x.dat","r");
    int count=0;
    double a,b;
    while (!feof(fin1) && count < n) 
    {
        fscanf(fin1, "%lf+%lfi \n", &a, &b);
        X[count] = CMPLX(a,b);
        count++;
    }
    
    /*Reading fft_h.dat*/
    fin2 = fopen("fft_h.dat","r");
    count=0;
    while (!feof(fin2) && count < n) 
    {
        fscanf(fin2, "%lf+%lfi \n", &a, &b);
        H[count] = CMPLX(a,b);
        count++;
    }

    /*Calculating fft of y=X*H*/
    for(int i=0;i<n;i++)
    {
        Y[i] = H[i]*X[i];
        ifft_Y[i] = Y[i];
    }

    /*Calculating inv fft of Y*/
	ifft(ifft_Y,n);
	fout1 = fopen("ifft_y.dat","w");
    for(int i=0;i<n;i++)
    {
        fprintf(fout1,"%lf \n",creal(ifft_Y[i]));
    }

    fclose(fin1);
    fclose(fin2);
    fclose(fout1);
    return 0;
    
}