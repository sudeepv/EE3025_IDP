#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <string.h>


/*FFT implemented in a divide and conquer approach using recursive calls*/
/*Ref:https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/*/
void fft(double complex* x, int n){
    
    /*Base case*/
    if (n == 1)
        return;

	/*Dividing the DFT into it's even and odd parts*/
	double complex* odd = malloc(n/2 * sizeof(double complex));
    double complex* even = malloc(n/2 * sizeof(double complex));
    for (int i = 0; 2*i<n; i++) {
        even[i] = x[2*i];
        odd[i] = x[2*i + 1];
    }

    /*Recursive calls to even and odd parts of DFT*/
    fft(even, n/2);
    fft(odd, n/2);

    /*Merging the even and odd parts of DFT*/
    double complex w; 
    for (int i = 0; 2 * i < n; i++) {
        w = CMPLX(cos(2*M_PI*i/n), sin(2*M_PI*i/n));
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
    double* x = (double*)malloc(n * sizeof(double));
    double* h = (double*)malloc(n * sizeof(double));
    
    double complex* X = (double complex*)malloc(n * sizeof(double complex));
    double complex* H = (double complex*)malloc(n * sizeof(double complex));
    
    FILE *fin1,*fin2,*fout1,*fout2;

    /*Reading x.dat*/
    fin1 = fopen("x.dat","r");
    int count=0;
    while (!feof(fin1) && count < n) 
    {
        fscanf(fin1, "%lf", &(x[count]));
        X[count] = CMPLX(x[count],0);
        count++;
    }
    
    /*Reading hn.dat*/
    fin2 = fopen("hn.dat","r");
    count=0;
    while (!feof(fin2) && count < n) 
    {
        fscanf(fin2, "%lf", &(h[count]));
        H[count] = CMPLX(h[count],0);
        count++;
    }

    /*Calculating fft of x*/
    fft(X,n);
    fout1 = fopen("fft_x.dat","w");
    for(int i=0;i<n;i++)
    {
        fprintf(fout1,"%lf+%lfi \n",creal(X[i]),cimag(X[i]));
    }

    /*Calculating fft of h*/
    fft(H,n);
    fout2 = fopen("fft_h.dat","w");
    for(int i=0;i<n;i++)
    {
        fprintf(fout2,"%lf+%lfi \n",creal(H[i]),cimag(H[i]));
    }

    
    fclose(fin1);
    fclose(fin2);
    fclose(fout1);
    fclose(fout2);
    return 0;
    
}