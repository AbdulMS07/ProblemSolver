/**
input: /u/love\i
output: iloveyou
**//

import java.util.*;
public class Bookshelf
{
	public static void main(String[] args) {
	   Scanner scan = new Scanner(System.in);
	   String s=scan.nextLine();
	   String res="";
		for(int i=1;i<s.length()-1;i++){
		    if(s.charAt(i)=='/' || s.charAt(i)=='\\'){
		        res=res+" ";
		        continue;
		    }
		    res=res+s.charAt(i);
		}
		String sarr[] =res.split(" ");
		for(int i=sarr.length-1;i>=0;i--){
		    System.out.print(sarr[i]);
		}
	}
}