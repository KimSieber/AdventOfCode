/**
 * Advent of Code
 *
 * Day 10
 *
 * Lange Problem gesucht, da Beispiele funktionierten als auch Marvins Puzzle bei mir funktionierte.
 * Problem lag in der Funktion minimizeDiff(), da bei Koordinaten (hoher) Primzahl, 0 der gemeinsame Teiler
 * falsch berechnet wurde.
 * Beispiele waren zu klein und Marvins Puzzle hatte überraschenderweise keinen Asteroiden auf einer Koordinate
 * mit Primzahl sitzen. Daher viele Stunden verwende.
 */
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
		 * Part Two: Zerstoere Asteroiden
		 **/
		destroyAsteroids dA = new destroyAsteroids();
		dA.setInputMap(MS.InputMap);
        dA.listVisibleAsteroids(result[0], result[1]);
        /** Belegungs-Regel:
	     *  ResultList[n][0] = x-Koordinate
	     *  ResultList[n][1] = y-Koordinate
	     *  ResultList[n][2] = DiffX
	     *  ResultList[n][3] = DiffY
	     *  ResultList[n][4] = Sortier-Wert auf Basis DiffX und DiffY
	     *  ==> public double[][] calcSortDivisor(double[][] Map, int PosDiffX, int PosDiffY, int PosResult) {
	     **/
        dA.ResultList = dA.calcSortDivisor(dA.ResultList, 2, 3, 4);
        dA.ResultList = dA.bubblesort(dA.ResultList, 4);
        //dA.printResultList();
        /** PARAMETER
         * destryAsteroids(int StopAtCounter)
         * 
         * RUECKGABEWERT
         * result[0] = letzte Koordinate x
         * result[1] = letzte Koordinate y
         * result[2] = Zaehler zerstoert (zur Kontrolle mit Parameter)
         **/
        int[] resultDest = dA.destryAsteroids(200);
        System.out.println("Anzahl zerstoerte Asteroiden = " + resultDest[2] + "   -> letzer an Position x|y = "+resultDest[0]+"|"+resultDest[1]);
        
        System.out.println("ready.");
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

/**
 * Part Two
 **/
class destroyAsteroids{
	private char[][] InputMap;
	/** Belegungs-Regel:
	 *  ResultList[n][0] = x-Koordinate
	 *  ResultList[n][1] = y-Koordinate
	 *  ResultList[n][2] = DiffX
	 *  ResultList[n][3] = DiffY
	 *  ResultList[n][4] = Sortier-Wert auf Basis DiffX und DiffY
	**/  
	public double[][] ResultList;
	
	public void setInputMap(char[][] inInputMap){
		this.InputMap = inInputMap;
		this.ResultList = new double[1][5];
		
	}
	
	public void listVisibleAsteroids(int x, int y){
        int count = 0;
        for (int y2=0; y2<this.InputMap.length; y2++) {
			for (int x2=0; x2<this.InputMap[0].length; x2++) {
				if (checkVisible(x, y, x2, y2)) {
				    if (count>this.ResultList.length-1) {
				        double[][] tmp = new double[count+1][5];
				        System.arraycopy(this.ResultList, 0, tmp, 0, this.ResultList.length);
				        this.ResultList = tmp;
				    }
				    double[] tmpRes = {x2, y2, x2-x, y2-y, 0};
					this.ResultList[count] = tmpRes;
					count++;
				}
			}
		}	    
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
		for (int i=(this.InputMap[0].length<this.InputMap.length ? this.InputMap.length : this.InputMap[0].length); i>0; i--) {
			if (result[0] % i == 0  &&
			    result[1] % i == 0 ) {
				result[0] = result[0] / i;
				result[1] = result[1] / i;
			}
		}	
		return result;
	}	

    public double[][] calcSortDivisor(double[][] Map, int PosDiffX, int PosDiffY, int PosResult) {
//System.out.println("calcSortDivisor[i]["+PosDiffX+"]["+PosDiffY+"]["+PosResult+"]");
        for (int i=0; i<Map.length; i++) {
//System.out.println("i="+i+"  Map.length="+Map.length+"   Map[0].length="+Map[0].length);
            Map[i][PosResult] = Map[i][PosDiffY] / Map[i][PosDiffX];
            if (Map[i][PosDiffX] == 0) {
                if (Map[i][PosDiffY] < 0) {
                    Map[i][PosResult] = 0;
                } else {
                    Map[i][PosResult] = 180;
                }
            } else {
                Map[i][PosResult] += (Map[i][PosDiffX]>0 ? 90 : 270);
            }
        }
        return Map;
    }
    
    public double[][] bubblesort(double[][] Map, int SortPos) {
		double[] temp;
		for(int i=1; i<Map.length; i++) {
			for(int j=0; j<Map.length-i; j++) {
				if(Map[j][SortPos]>Map[j+1][SortPos]) {
					temp=Map[j];
					Map[j]=Map[j+1];
					Map[j+1]=temp;
				}
				
			}
		}
		return Map;
	}

        /** PARAMETER
         * destryAsteroids(int StopAtCounter)
         * 
         * RUECKGABEWERT
         * result[0] = letzte Koordinate x
         * result[1] = letzte Koordinate y
         * result[2] = Zaehler zerstoert (zur Kontrolle mit Parameter)
         **/
	public int[] destryAsteroids(int StopAtCounter) {
	    int x=0, y=0, count=0;
	    for (int i=0; i<this.ResultList.length; i++) {
	        x = (int)this.ResultList[i][0];
	        y = (int)this.ResultList[i][1];
	        this.InputMap[y][x] = '0';
	        count ++;
	        if (StopAtCounter == count) {
	            int[] result= {x, y, count};
	            return result;
	        }
	    }
	    int[] result = {x, y, count};
	    return result;
	}
	
	public void printResultList() {
		for (int i=0; i<this.ResultList.length; i++) {
		    for (int j=0; j<this.ResultList[0].length; j++) {
		        System.out.print(this.ResultList[i][j]+"   ");
		    }
            System.out.println("");
    	}
    }
}
