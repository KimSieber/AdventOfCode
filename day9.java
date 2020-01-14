```Java

import java.util.Scanner;
import java.util.Arrays;

class IncodeComputer{
	private Scanner reader;
	private String[] vProg;
	private Integer vPointer, vInst, vIdx1, vIdx2, vIdx3, vRelativeBase;

	public IncodeComputer(){
		this.reader = new Scanner(System.in);
		this.vProg = this.readLine().split(",");
		this.vPointer = 0;
		this.vRelativeBase = 0;
	}
	
	private String readLine(){
	    return this.reader.nextLine();
	}
	
	private Long getValue(int pIndex){
		if (pIndex > (this.vProg.length-1)) {
			return Long.parseLong("0");
		} else {
			if (this.vProg[pIndex]==null){
				return Long.parseLong("0");
			} else {
				return Long.parseLong(this.vProg[pIndex]);
			}
		}
	}
	
	private void setValue(int pIndex, long pValue){
		if (pIndex > this.vProg.length-1) {
			vProg = Arrays.copyOf(vProg, pIndex+1);
		}
		vProg[pIndex] =Long.toString(pValue);
	}
	
	private void printValue(int pIndex){
		System.out.println(this.vProg[pIndex]);
	}
	
	private void readInstruction(){
		int Mod1, Mod2, Mod3;
	
		String Instruc ="0000"+this.vProg[this.vPointer];
		Instruc = Instruc.substring(Instruc.length()-5);
		
		this.vInst = Integer.parseInt(Instruc.substring(3,5));
		
		Mod1 = Integer.parseInt(Instruc.substring(2,3));
		Mod2 = Integer.parseInt(Instruc.substring(1,2));
		Mod3 = Integer.parseInt(Instruc.substring(0,1));
		
		//System.out.println("Instruc ="+(Instruc)+"   vInst="+this.vInst);
		
		this.vIdx1=this.getIndex(Mod1, this.vPointer+1);
		this.vIdx2=this.getIndex(Mod2, this.vPointer+2);
		this.vIdx3=this.getIndex(Mod3, this.vPointer+3);
		
/*
		System.out.println("Mod1="+(Mod1)+"  vIdx1="+this.vIdx1);
		System.out.println("Mod2="+(Mod2)+"  vIdx2="+this.vIdx2);
		System.out.println("Mod3="+(Mod3)+"  vIdx3="+this.vIdx3);
*/
	}
	
	private Integer getIndex(int pMode, int pIdx){
		switch(pMode){
			case 0:
				return getValue(pIdx).intValue();
			case 1:
				return pIdx;
			case 2:
				return getValue(pIdx).intValue() + vRelativeBase;
		}
		return null;
	}
	
	private void runDiagnostic (){
		switch (vInst) {
			case 99:
				System.exit(0);
			case 1:
				setValue(vIdx3, getValue(vIdx1) + getValue(vIdx2));
				vPointer += 4;
				break;
			case 2:
				setValue(vIdx3, getValue(vIdx1) * getValue(vIdx2));
				vPointer += 4;
				break;
			case 3:
				setValue(vIdx1, Long.parseLong(this.readLine()));
				vPointer += 2;
				break;
			case 4:
				this.printValue(vIdx1);
				vPointer += 2;
				break;
			case 5:
				if (getValue(vIdx1).intValue() != 0) { 
				    vPointer = getValue(vIdx2).intValue();
				} else { 
				    vPointer += 3; 
				}
				break;
			case 6:
				if (getValue(vIdx1).intValue() == 0) {
					vPointer = getValue(vIdx2).intValue();
				} else {
					vPointer += 3;
				}
				break;
			case 7:
				if (getValue(vIdx1) < getValue(vIdx2)) {
					setValue(vIdx3, 1);
				} else {
					setValue(vIdx3, 0);
				}
				vPointer += 4;
				break;
			case 8:
				if (getValue(vIdx1) == getValue(vIdx2)) {
					setValue(vIdx3, 1);
				} else {
					setValue(vIdx3, 0);
				}
				vPointer += 4;
				break;
			case 9:
				vRelativeBase += getValue(vIdx1).intValue();
			    vPointer += 2;
				break;
		}
	}
	
	public void runIntcodeComputer(){
		for (int i = 0; i < 10000000; i++) {
			this.readInstruction();
			this.runDiagnostic(); 
		}
	}
}

public class Day9{
    public static void main(String args[]){
		IncodeComputer IC = new IncodeComputer();
		
		IC.runIntcodeComputer();
		
		System.out.println("ready.");
    }
}

```
