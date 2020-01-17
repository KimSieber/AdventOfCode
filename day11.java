import java.util.Scanner;
import java.util.Arrays;

public class day11{
    public static void main(String args[]){
		IncodeComputer IC = new IncodeComputer();
		
		int[] ReturnValues = IC.runIntcodeComputer(0);
		System.out.println("ReturnValues = "+ReturnValues[0]+" | "+ReturnValues[1]);

		System.out.println("ready.");
    }
}

class IncodeComputer{
	private Scanner reader;
	private String[] vProg;
	private Integer vPointer=0, vInst, vIdx1, vIdx2, vIdx3, vRelativeBase=0;
	
	private int countRV;
	private int[] ReturnValues = new int[2];

	public IncodeComputer(){
		this.reader = new Scanner(System.in);
		this.vProg = this.reader.nextLine().split(",");
	}
	
	public int[] runIntcodeComputer(int Input){
	    this.countRV = 0;
		for (int i = 0; i < 1000; i++) {
			this.readInstruction();
			if(!this.runDiagnostic(Input)) {
			    return ReturnValues;                ==> wenn 99 behandeln
			}
		}
		System.out.println("runIntcodeComputer:ERROR");
		return null;
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
	
	private void readInstruction(){
		int Mod1, Mod2, Mod3;
	
		String Instruc ="0000"+this.vProg[this.vPointer];
		Instruc = Instruc.substring(Instruc.length()-5);
		
		this.vInst = Integer.parseInt(Instruc.substring(3,5));
		
		Mod1 = Integer.parseInt(Instruc.substring(2,3));
		Mod2 = Integer.parseInt(Instruc.substring(1,2));
		Mod3 = Integer.parseInt(Instruc.substring(0,1));

		this.vIdx1=this.getIndex(Mod1, this.vPointer+1);
		this.vIdx2=this.getIndex(Mod2, this.vPointer+2);
		this.vIdx3=this.getIndex(Mod3, this.vPointer+3);
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
	
	private boolean runDiagnostic (int pInput){
		switch (this.vInst) {
			case 99:
				return false;
			case 1:
				this.setValue(this.vIdx3, this.getValue(this.vIdx1) + this.getValue(this.vIdx2));
				vPointer += 4;
				break;
			case 2:
				this.setValue(this.vIdx3, this.getValue(this.vIdx1) * this.getValue(this.vIdx2));
				vPointer += 4;
				break;
			case 3:
				this.setValue(this.vIdx1, pInput);
				this.vPointer += 2;
				break;
			case 4:
				this.ReturnValues[this.countRV] = Integer.parseInt(this.vProg[this.vIdx1]);
				this.countRV++;
				this.vPointer += 2;
				if (this.countRV > 1) {
				    return false;
				}
				break;
			case 5:
				if (this.getValue(this.vIdx1).intValue() != 0) { 
				   this. vPointer = this.getValue(this.vIdx2).intValue();
				} else { 
				    this.vPointer += 3; 
				}
				break;
			case 6:
				if (this.getValue(this.vIdx1).intValue() == 0) {
					this.vPointer = this.getValue(this.vIdx2).intValue();
				} else {
					this.vPointer += 3;
				}
				break;
			case 7:
				if (this.getValue(this.vIdx1) < this.getValue(this.vIdx2)) {
					this.setValue(this.vIdx3, 1);
				} else {
					this.setValue(this.vIdx3, 0);
				}
				this.vPointer += 4;
				break;
			case 8:
				if (this.getValue(this.vIdx1) == this.getValue(this.vIdx2)) {
					this.setValue(this.vIdx3, 1);
				} else {
					this.setValue(this.vIdx3, 0);
				}
				this.vPointer += 4;
				break;
			case 9:
				this.vRelativeBase += this.getValue(this.vIdx1).intValue();
			    this.vPointer += 2;
				break;
		}
		return true;
	}
}
