class Solution {
    public int[] plusOne(int[] digits) {
        int len = digits.length;
        
        // int sum=digits[len-1];
        
        // if(len>1){
        //     int j=1;
        //     for(int i =len-2;i>=0;i--){
        //     System.out.print(sum);
        //     sum+= digits[i]*Math.pow(10,j);
        //     j++;
        //     }
        // }
        // // System.out.print(sum);
        // sum +=1;
        // int newarr[] = convertIntToArray(sum);
        if(digits[len-1]+1 ==10 ){
            int temp = 0;
            for(int i=len-1;i>=0;i--){
                if(digits[len-1]+1 ==10){
                    temp=1;
                    digits[i] =0;
                    
                }
                else if(temp ==1){
                    if(digits[i]+1 ==10){
                        digits[i] =0;
                        temp =1;
                    }
                    else{
                        digits[i] =digits[i] +1;
                        temp = 0;
                    }
                }
                else{
                    temp = 0;
                }
            }
           if(digits[0]==0){
               int newarr[] = new int[len+1];
               newarr[0]=1;
               for(int i=1;i<len+1;i++){
                   newarr[i]=0;
               }
               return newarr;
           }
           else{
               return digits;
           }
            // int newarr[] = new int[len+1];
            
        }
        else{
            digits[len-1] = digits[len-1]+1;
            return digits;
        }
       
    }
    // //convert int to array
    // public int[] convertIntToArray(int number) {
    //     // Count the number of digits in the number
    //     int numDigits = (int) Math.log10(number) + 1;
        
    //     // Create an array to store the digits
    //     int[] digits = new int[numDigits];
        
    //     // Extract the digits and store them in the array
    //     for (int i = numDigits - 1; i >= 0; i--) {
    //         digits[i] = number % 10;
    //         number /= 10;
    //     }
        
    //     return digits;
    // }
}