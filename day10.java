import java.util.Scanner;
import java.io.*;

public class Day10{
    public static void main(String args[]){
		MonitoringStation MS = new MonitoringStation();
		MS.runCheck();
		int[] result = MS.getHighValue();
		System.out.println("Höchster Wert:"+result[2]+" an x/y="+result[0]+"|"+result[1]);
		System.out.println("ready.");
    }
}

class MonitoringStation{
	private static final int maxY = 20;
	private int maxX;

	private Scanner reader;
	private char[][] InputMap;
	private int[][] ResultMap;
	
	public MonitoringStation(){
		this.reader = new Scanner(System.in);
		String inputLine = this.reader.nextLine();
		this.maxX = inputLine.length();
		this.InputMap = new char[maxY][maxX];
		this.ResultMap = new int[maxY][maxX];
		
		this.InputMap[0] = inputLine.toCharArray(); 
		
		int i = 0;
		while (reader.hasNextLine()){
			i++;
			inputLine = this.reader.nextLine();
			this.InputMap[i] = inputLine.toCharArray();
		}
	}
	
	public void runCheck(){
		for (int y=0; y<this.maxY; y++) {
			for (int x=0; x<this.maxX; x++) {
				if (this.InputMap[y][x] == '#') {
					
					this.ResultMap[y][x] = this.countVisible(x,y);
					//if (x==11 && y==13) {
						
					
				//System.out.println("ResultMap["+y+"]["+x+"]="+ this.ResultMap[y][x]);}
				}
				
			}
		}
	}
	
	private int countVisible(int x1, int y1){
		int count = 0;
	
		for (int y=0; y<this.maxY; y++) {
			for (int x=0; x<this.maxX; x++) {
				if (checkVisible(x1, y1, x, y)) {
					
					count++;
				}
			}
		}
		return count;
	}
	
	private boolean checkVisible(int x1, int y1, int x2, int y2) {
		
		// wenn sich selbst gefunden
		if (x1==x2 && y1==y2) { return false; }
		// wenn kein Asteroid
		if (this.InputMap[y2][x2] != '#') { return false; }
		
		int DiffX = x2 - x1;
		int DiffY = y2 - y1;
		
		int[] MinDiff = this.minimizeDiff(DiffX, DiffY);
		int MinDiffX = MinDiff[0];
		int MinDiffY = MinDiff[1];
		
		int tmpX, tmpY;
		int MDX = (MinDiffX>0?MinDiffX:MinDiffX*-1);
		int MDY = (MinDiffY>0?MinDiffY:MinDiffY*-1);
		int iCnt = (MDX>MDY ? DiffX/MinDiffX : DiffY/MinDiffY);

if (x1==11 && y1==13) {
System.out.println("checkVisible("+x1+","+y1+","+x2+","+y2+")  iCnt="+iCnt+"  ->DiffX,Y="+DiffX+","+DiffY+"  MinDiffX,Y="+ MinDiffX+","+ MinDiffY);

}
		
		for (int i=1; i<=iCnt; i++) {
			tmpX = x1+(MinDiffX * i);
			tmpY = y1+(MinDiffY * i);
			if (this.InputMap[tmpY][tmpX] == '#') {
				if (x2 == tmpX && y2 == tmpY) {
					
					
					if (x1==11 && y1==13) {
//System.out.println("checkVisible("+x1+","+y1+","+x2+","+y2+")==true");
//System.out.println("  ->tmpX="+tmpX+",tmpY="+tmpY);
					
					}
				
					return true;
				} else {
					return false;
				}
			}
		}
		return true;
	}
	
	private int[] minimizeDiff(int DiffX, 
	                           int DiffY) {
		int[] result = {DiffX, DiffY};
		if (DiffX== 1|| DiffY== 1 ||
		    DiffX==-1|| DiffY==-1 ) {
			return result;
		}
		for (int i=10; i>0; i--) {
			if (result[0] % i == 0 &&
			    result[1] % i == 0) {
				
			    result[0] = result[0] / i;
				result[1] = result[1] / i;
			}
		}
		
		//System.out.println("minimizeDiff("+ DiffX +","+ DiffY +") || result[]={"+ result[0] +","+ result[1]+"}");
		
		return result;
	}
	
	public int[] getHighValue() {
		int MaxX=0, MaxY=0, MaxScore=0;
		for (int y=0; y<this.maxY; y++) {
			for (int x=0; x<this.maxX; x++) {
				if (ResultMap[y][x]>MaxScore) {
					MaxScore = ResultMap[y][x];
					MaxX = x;
					MaxY = y;
				}
			}
		}
		int[] result = {MaxX, MaxY, MaxScore};
		return result;
	}
}

