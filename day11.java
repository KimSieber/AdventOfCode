import java.util.Scanner;
import java.util.Arrays;

public class day11{
    public static void main(String args[]){
		PaintingRobot PR = new PaintingRobot();
		
		System.out.println("ready.");
    }
}

class PaintingRobot {
    IncodeComputer ICC;
    /** PanelMap-Belegung ******
     *  -1 = schwarz, aber noch nicht gestrichen
     *  0    = schwarz gestrichen
     *  1    = weiss gestrichen
     * 
     *  Koordinaten [y][x]
     **/
    int[][] PanelMap = new int[500][500];
    /** Koordinaten von ActPos *********
     *  0 = x-Wert
     *  1 = y-Wert
     **/
    int[] actPos = {250, 250};
    /** direction-Belegung ******
     *  0 = ^  (nach oben)
     *  1 = >  (nach rechts)
     *  2 = v  (nach unten
     *  3 = <  (nach links)
     **/
    int direction = 0;
    
    public PaintingRobot(){
        IncodeComputer IC = new IncodeComputer();
        /** 
         * Initialisiere Panel-Map mit -1
         **/
        for (int i=0; i<this.PanelMap.length; i++) {
            for (int j=0; j<this.PanelMap[0].length; j++) {
                this.PanelMap[i][j] = -1;
            }
        }
        int ret;
		do {
		    ret = IC.runIntcodeComputer(this.getColor());
    		if (ret!=99) {
    		    this.paintPanel(IC.ReturnValues[0]);
    		    this.turnAndMove(IC.ReturnValues[1]);
    		    //System.out.println("ReturnValues = "+ReturnValues[0]+" | "+ReturnValues[1]);
    		}
		} while(ret != 99);
        int cPP = countPaintedPanels();
        System.out.println("countPaintedPanels = "+cPP);
    }

    private int getColor() {
        int x = this.actPos[0];
        int y = this.actPos[1];
        
        if (this.actPos[0]<10 || this.actPos[1]<10) {
            System.out.println("Koordinaten reichen nicht aus?: actPos="+x+"|"+y);
        }
        
        return (this.PanelMap[y][x]<0 ? 0 : this.PanelMap[y][x]);
    }
    
    private void paintPanel(int color) {
        this.PanelMap[this.actPos[1]][this.actPos[0]] = color;
    }
    
    private void turnAndMove(int turn) {
        if (turn == 0) {
            this.direction -= 1;
        } else {
            this.direction += 1;
        }
        if (this.direction < 0) {
            this.direction = 3;
        }
        if (this.direction > 3) {
            this.direction = 0;
        }
        switch (this.direction) {
            case 0:
                this.actPos[1] -= 1;
                break;
            case 1:
                this.actPos[0] += 1;
                break;
            case 2:
                this.actPos[1] += 1;
                break;
            case 3:
                this.actPos[0] -= 1;
                break;
            default:
                System.out.println("Error turnAndMove("+turn+") this.direction="+this.direction);
                System.exit(-1);
        }
    }
    
    private int countPaintedPanels() {
        int count = 0;
        for (int y=0; y<this.PanelMap.length; y++) {
            for (int x=0; x<this.PanelMap.length; x++) {
                if (this.PanelMap[y][x] != -1) {
                    count++;
                }
            }
        }
        return count;
    }
}

class IncodeComputer{
	private Scanner reader;
	private String[] vProg;
	private Integer vPointer=0, vInst, vIdx1, vIdx2, vIdx3, vRelativeBase=0;
	
	private int countRV;
	public int[] ReturnValues = new int[2];

	public IncodeComputer(){
		this.reader = new Scanner(System.in);
		this.vProg = this.reader.nextLine().split(",");
	}
	
	/**
	 * Rueckgabewerte:
	 * 99 = Programm endet
	 *  0 = Beide Rueckgabewerte gefuellt, Programm bereit zum weiter machen
	 **/
	public int runIntcodeComputer(int Input){
	    this.countRV = 0;
		for (int i = 0; i < 1000; i++) {
			this.readInstruction();
			switch(this.runDiagnostic(Input)) {
			    case 99:
			        return 99;
    			case 0:
    			    return 0;
    			case 1: 
    			    // Verarbeitet, naechster Befehl
    			    break;
			}
		}
		System.out.println("runIntcodeComputer:ERROR");
		return 99;
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
	
	/**
	 * Rueckgabewerte:
	 * 99 = Ende des Programms
	 *  0 = Beide Rueckgabewerte gefuellt
	 *  1 = Komando ausgefuehrt, weiter
	 **/
	private int runDiagnostic (int pInput){
		switch (this.vInst) {
			case 99:
				return 99;
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
				    return 0;
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
		return 1;
	}
}
