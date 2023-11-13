// See https://aka.ms/new-console-template for more information
using System;

namespace Gaussian_elimination
{
    class Gaus{
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

        static void Swapping(double [,] arr,int max_i,int j)
        {
            for (int k=j; k<arr.GetLength(1); k++){
                (arr[max_i,k],arr[j,k])=(arr[j,k],arr[max_i,k]);
            }
        }

        static void Dimensions(double [,] arr,int a)
        {
            double mn=0;
            int k=arr.GetLength(1);
            double [] arr2=new double [k];
            for (int i=a+1; i<arr.GetLength(1)-1; i++){
                mn=-(arr[i,a]/arr[a,a]);
                for(int n=0; n<arr.GetLength(1); n++){
                    arr2[n]=arr[a,n]*mn;
                    arr[i,n]=arr[i,n]+arr2[n];


                }
            }
        }
        
        static void PrintRes(double [] arr){
            for (int i=0; i<arr.GetLength(0); i++){
                Console.WriteLine("x"+(i+1)+" = "+Math.Round(arr[i],4));
            }
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
        static void Gaus_F(double [,] arr)
        {
            int count_p=0;
            for(int j=0; j<arr.GetLength(0); j++){
                double max=0;
                int max_i=-1;
                for(int i=j; i<arr.GetLength(0); i++){
                    if (Math.Abs(arr[i,j])>max){
                        max=Math.Abs(arr[i,j]);
                        max_i=i;
                    }
                }
                if (max>Math.Pow(10,-6)){
                    if(max_i!=j){count_p++;}
                    Swapping(arr,max_i,j);
                    Dimensions(arr,j);
                }
                // else{
                //     arr[max_i,j]=0;
                // }
            }
            double vyzn=1;
            for (int i=0; i<arr.GetLength(0); i++){
                vyzn=vyzn*arr[i,i];
            }
            vyzn=vyzn*Math.Pow(-1,count_p);
            Console.WriteLine("Vyznachnyk: "+vyzn);
            double [] res=Enumerable.Repeat(1.0,arr.GetLength(0)).ToArray();
            int v=arr.GetLength(1)-1;
            bool is_sol=true;
            for (int i=arr.GetLength(0)-1;i>=0;i--){
                double s=0;
                for (int j=0;j<v;j++){
                    if (j!=i){
                        s+=arr[i,j]*res[j];
                    }
                }
                if ((arr[i,v]-s)==0 && arr[i,i]==0 && is_sol==true){
                    Console.WriteLine("Infinite number of solutions for x" +i);
                }else if((arr[i,v]-s)!=0 && arr[i,i]==0){
                    Console.WriteLine("!---- NO SOLUTIONS FOUND ----!  Do not take into consideration all the solutions listed below or above");
                    is_sol=false;
                    break;
                }
                else{
                    res[i]=(arr[i,v]-s)/arr[i,i];
                }
                
            }
            if(is_sol==true){PrintRes(res);}

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
            Console.WriteLine("----------------RESULTS----------------");
            Gaus_F(a);
            Console.WriteLine("Result Matrix");
            PrintMtx(a);
        }
    }
}
