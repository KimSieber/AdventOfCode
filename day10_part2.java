import java.util.Scanner;
import java.io.*;

public class day10_part2{

    public static void main(String args[]){
		/**
		 * Part One: Ermittle Asteroiden mit bester Sicht
		 **/
		MonitoringStation MS = new MonitoringStation();
		MS.runCheck();
		int[] result = MS.getHighValue();
		System.out.println("Hoechster Wert:"+result[2]+" an x/y="+result[0]+"|"+result[1]);
		
		/**
		 * Part Two: Zerstöre Asteroiden
		 **/
		

        
    }
}

/**
 * Part One
 */
class MonitoringStation{
	private Scanner reader;
	private int maxX, maxY;
	public char[][] InputMap;
	private int[][] ResultMap;
	
	public MonitoringStation(){
		this.reader = new Scanner(System.in);
		String inputLine = this.reader.nextLine();
		this.maxX = inputLine.length();
		this.InputMap = new char[1][maxX];
		this.InputMap[0] = inputLine.toCharArray(); 
		int i = 0;
		while (reader.hasNextLine()){
			i++;
			inputLine = this.reader.nextLine();
			char[][] tmp = new char[i+1][maxX];
            		System.arraycopy(this.InputMap, 0, tmp, 0, i);
			this.InputMap = tmp;
			this.InputMap[i] = inputLine.toCharArray();
		}
		this.maxY = i+1;
		this.ResultMap = new int[maxY][maxX];
	}
	
	public void runCheck(){
		for (int y=0; y<this.maxY; y++) {
			for (int x=0; x<this.maxX; x++) {
				if (this.InputMap[y][x] == '#') {
					this.ResultMap[y][x] = this.countVisible(x,y);
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
		// Differenzen suchen
		int DiffX = x2 - x1;
		int DiffY = y2 - y1;
		// Minimale Differenz suchen, um "Linie" abzusuchen
		int[] MinDiff = this.minimizeDiff(DiffX, DiffY);
		int MinDiffX = MinDiff[0];
		int MinDiffY = MinDiff[1];
		// Vorzeichen entfernen um hoechsten Zaehler fuer Schleife zu finden (Weg von xy1 zu xy2)
		int MDX = (MinDiffX<0?MinDiffX*-1:MinDiffX);
		int MDY = (MinDiffY<0?MinDiffY*-1:MinDiffY);
		int iCnt = (MDX>MDY ? DiffX/MinDiffX : DiffY/MinDiffY);
		// In Schleife Weg von xy1 zu xy2 abfahren und pruefen, wann erster Asteroid (=#) auftraucht
		int tmpX, tmpY;	
		for (int i=1; i<=iCnt; i++) {
			tmpX = x1+(MinDiffX * i);
			tmpY = y1+(MinDiffY * i);
			// Wenn ein Asteroid gefunden ...
			if (this.InputMap[tmpY][tmpX] == '#') {
				// ... pruefen, ob es der gepruefte Asteroid (xy2) ist
				if (x2 == tmpX && y2 == tmpY) {
					// Wenn ja, dann ist xy2 in Sichtlinie zu xy1
					return true;
				} else {
					// Wenn anderer Asteroid gefunden, dann ist xy2 verdeckt -> nicht in Sichtlinie
					return false;
				}
			}
		}
		return true;
	}
	
	private int[] minimizeDiff(int DiffX, int DiffY) {
		int[] result = {DiffX, DiffY};
		// Bei 1 ist keine Division moeglich, daher direkt Eigabe als MinimalDifferenz zurueckgeben
		if (DiffX== 1 || DiffY== 1 ||
		    DiffX==-1 || DiffY==-1 ) {
			return result;
		}
		// Divisionen pruefen, um Minimal-Differenz zu ermitteln, Zaehler als Anzahl Zeilen/Spalten = hoechster dividierbarer Wert
		for (int i=(this.maxX<this.maxY ? this.maxY : this.maxX); i>0; i--) {
			if (result[0] % i == 0  &&
			    result[1] % i == 0 ) {
				result[0] = result[0] / i;
				result[1] = result[1] / i;
			}
		}	
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
	
	public void printMap() {
		String tmp = " ";
		for (int y=0; y<this.maxY; y++) {
			for (int x=0; x<this.maxX; x++) {
	            		tmp = tmp + this.InputMap[y][x];
	        	}
	        	System.out.println(tmp);
	        	tmp = " ";
	    	}
	}
}


class destroyAsteroids{
	private char[][] InputMap;
	/** Belegungs-Regel:
	 *  ResultList[n][0] = x
	 *  ResultList[n][0] = x
	 *  ResultList[n][0] = x
	 *  ResultList[n][0] = x
	 *  ResultList[n][0] = x
	**/
	
	private double[][] ResultList;
	
	public void setInputMap(char[][] inInputMap){
		this.InputMap = inInputMap;
		this.ResultList = new double[1][5];
		
	}
}
