using System;
using System.Numerics;
using System.IO;
using MathNet.Numerics.LinearAlgebra;
using MathNet.Numerics.LinearAlgebra.Double;

namespace LU_Elimination
{
    class LU_el{
        static void ReadMtx(double[,] arr,int a, int b)
        { 
            String input =File.ReadAllText("what3.txt");
            foreach (var row in input.Split('\n'))
            {
                b=0;
                foreach (var col in row.Trim().Split(' '))
                {
                    arr[a,b]=double.Parse(col.Trim());
                    b++;
                    
                }
                a++;
            }
        }
    
        
        static void PrintRes(double [] arr){
            for (int i=0; i<arr.GetLength(0); i++){
                Console.WriteLine("x"+(i+1)+" = "+Math.Round(arr[i],4));
            }
        }

        static double Suma(double [,] L, double[,] U,int i,int j, int m){
            double sum=0;
            for (int k=0;k<m;k++){
                sum=sum+L[i,k]*U[k,j];
            }
            return sum;
        }

        static void PrintMtx(double [,] arr)
        {
            for (int i=0; i<arr.GetLength(0); i++){
                for (int j=0; j<arr.GetLength(1); j++){
                    Console.Write(string.Format("{0} ", arr[i, j]));
                }
                Console.Write(Environment.NewLine + Environment.NewLine);
            }
        }

       static bool GetLeadingMinors(double[,] arr)
       {
        bool res=true;
        DenseMatrix matrix = DenseMatrix.OfArray(arr);
        for (int i = 0; i < matrix.RowCount; i++)
        {
            DenseMatrix minor = matrix.SubMatrix(0, i, 0, i) as DenseMatrix;
            double leadingMinor = minor.Determinant();
            if (leadingMinor==0){res=false;}
        }
        return res;
       }

       static double Check(double [] x, double [,] arr)
        {
            double result=0;
            double [] res=new double[x.GetLength(0)];
            double [] v=Enumerable.Repeat(0.0,x.GetLength(0)).ToArray();
            for (int i=0; i<arr.GetLength(0); i++){
                for (int j=0; j<arr.GetLength(0); j++){
                    v[i]=v[i]+x[j]*arr[i,j];
                }
            }
            MathNet.Numerics.LinearAlgebra.Vector<double> vector = DenseVector.OfArray(v);
            int last=arr.GetLength(0);
            for (int i=0;i<res.GetLength(0); i++){

                res[i]=Math.Pow((arr[i,last]-v[i]),2);
                result=result+res[i];
            }
            result=Math.Sqrt(result);
            return result;
        }
        

        static double [] L_slar(double [,] arr, double [,] L){
            double [] y=Enumerable.Repeat(1.0,arr.GetLength(0)).ToArray();
            double [] b=new double[arr.GetLength(0)];
            for (int i=0; i<arr.GetLength(0); i++){
                b[i]=arr[i,arr.GetLength(1)-1];
            }
            bool is_sol=true;
            for (int i=0; i<y.GetLength(0); i++){
                double s=0;
                for (int j=0; j<i+1; j++){
                    if (j!=i){
                        s+=L[i,j]*y[j];
                    }
                }
                if ((b[i]-s)==0 && L[i,i]==0 && is_sol==true){
                    Console.WriteLine("Infinite number of solutions for x" +i);
                }else if((b[i]-s)!=0 && L[i,i]==0){
                    Console.WriteLine("!---- NO SOLUTIONS FOUND ----!  Do not take into consideration all the solutions listed below or above");
                    is_sol=false;
                    break;
                }
                else{
                    y[i]=(b[i]-s)/L[i,i];
                }
            }
            return y;

        }

        static double [] U_slar(double [,] arr, double [,] U, double [] y){
            double [] x=Enumerable.Repeat(1.0,arr.GetLength(0)).ToArray();
            bool is_sol2=true;
            for (int i=x.GetLength(0)-1; i>=0; i--){
                double s=0;
                for (int j=i; j<x.GetLength(0); j++){
                    if (j!=i){
                        s+=U[i,j]*x[j];
                    }
                }
                if ((y[i]-s)==0 && U[i,i]==0 && is_sol2==true){
                    Console.WriteLine("Infinite number of solutions for x" +i);
                }else if((y[i]-s)!=0 && U[i,i]==0){
                    Console.WriteLine("!---- NO SOLUTIONS FOUND ----!  Do not take into consideration all the solutions listed below or above");
                    is_sol2=false;
                    break;
                }
                else{
                    x[i]=(y[i]-s)/U[i,i];
                }
            }
            return x;

        }

        
        static double LU_F(double [,] arr)
        {
            int size=arr.GetLength(0);
            double[,] L=new double [size,size];
            double[,] U=new double [size,size];

            for (int i=0; i<size; i++){
                for (int j=0; j<size; j++){
                    if(i==j){
                        U[i,j]=1;
                    }else if(i>j){
                        U[i,j]=0;
                    }else if(i<j){
                        L[i,j]=0;
                    }
                
                }
            }
            for (int i=0; i<size; i++){
                for (int j=0; j<i+1; j++){
                    L[i,j]=arr[i,j]-Suma(L,U,i,j,j);
                }
                for(int q=i+1; q<size; q++){
                    U[i,q]=(arr[i,q]-Suma(L,U,i,q,i))/L[i,i];
                }
            }
                PrintMtx(L);
                Console.WriteLine();
                PrintMtx(U);
                double []y=L_slar(arr,L);
                double []x=U_slar(arr,U,y);
                PrintRes(x);


            double determinant=1;
            for (int i=0; i<size; i++){
                    determinant*=L[i,i]*U[i,i];
            }

            if (Check(x,arr)<Math.Pow(10,-9)){Console.WriteLine("Pohybka mala");}

            return determinant;

        }


        


        static void Main(string [] args){
            int i=0,j=0;
            double[,] a=new double [3,4];
            Console.WriteLine("Read from file or console?");
            Console.WriteLine("1 - file");
            Console.WriteLine("2 - console");
            int num1 = int.Parse(Console.ReadLine());
            switch(num1){
                case 1:
                    ReadMtx(a,i,j);
                   break;
                case 2:
                    Console.WriteLine( "Enter the numbers" );
                    for ( int n = 0; n < a.GetLength(0); n++ )
                    {
                        for ( int m = 0; m < a.GetLength(1); m++ )
                        {
                            a[ n, m ] = Convert.ToDouble( Console.ReadLine( ) );
                        }
                    }
                    break;
                default:
                    break;
            }
            if(GetLeadingMinors(a)!=false){
                Console.WriteLine("Determinant "+LU_F(a));
            }else{
                Console.WriteLine("Minor=0");
            }
        }
    }
}
