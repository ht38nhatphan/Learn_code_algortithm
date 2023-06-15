package corejava;

public class Atoi {
	public static void main(String[] args) {
		int a = 3999;
		int i = intToRoman(a);
//		int j = Integer.parseInt(a);
		System.out.println(i);
	}
  //solution 
   public String intToRoman1(int num) {
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] romanl = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        StringBuilder roman = new StringBuilder();
        for(int i=0;i<values.length;i++){
            while(num >= values[i]){
                num = num-values[i];
                roman.append(romanl[i]);
            }
        }
        return roman.toString();
    }
	    public String intToRoman(int num) {
        String[] dv = {"I","II","III","IV","V","VI","VII","VIII","IX"};
        String[] tr = {"X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        String[] ng = {"C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        String[] cng = {"M","MM","MMM"};
        ArrayList<Integer> arr = new ArrayList<>();
        String str="";
        if(num == 1){
            return "I";
        }
        else if(num==5){
            return "V";
        }
        else if(num==10){
            return "X";
        }
        else if(num == 50){
            return "L";
        }
        else if(num==100){
            return "C";
        }
        else if(num==500){
            return "D";
        }
        else if(num==1000){
            return "M";
        }
        while(num>0){
            arr.add(num%10);
            System.out.print(num%10);
            num = num/10;
        }
        int i = arr.size();
        int len = arr.size();
        
        while(i>0){
             if(arr.get(i-1)==0){
                i-=1;
            }
            else if(i==4){
                str+= cng[arr.get(i-1)-1];
                i -=1;
            }
            else if(i==3){
                str+= ng[arr.get(i-1)-1];
                i -=1;
            }
            else if(i==2){
                str+= tr[arr.get(i-1)-1];
                i -=1;
            }
            
             else if(i==1 && arr.get(i-1)!=0){
                str+= dv[arr.get(i-1)-1];
                i -=1;

            }
           
            
        }
        return str;
    }
}
