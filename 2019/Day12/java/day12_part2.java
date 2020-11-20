/**
 * Advent of Code
 * 
 * Day 12 - Part Two
 * 
 * Teil 2 nur lösen können, mit nachkodierung von Marvins Lösung.
 * Lösungsweg inzwischen verstanden, aber selbst nicht drauf gekommen
 * => Suche nach der Anzahl Steps, an denen eine Achse (x, y oder z) wieder auf Ausgangswert ist
 * => Multipliziere die Step-Werte mit suche nach kleinstem, gemeinsamen nenner (da kleinster Wert gesucht) 
 */
public class day12 {
    /**
     * Main-Class
     * 
     * @param args[]
     */
    public static void main(String args[]) {
        moon[] mo = new moon[4];
        /**
         * Example 1
         *
        mo[0] = new moon("Io",       -1,  0,  2);
        mo[1] = new moon("Europa",    2,-10, -7);
        mo[2] = new moon("Ganymede",  4, -8,  8);
        mo[3] = new moon("Callisto",  3,  5, -1); */

        /**
         * Example 2
         *
        mo[0] = new moon("Io",       -8,-10,  0);
        mo[1] = new moon("Europa",    5,  5, 10);
        mo[2] = new moon("Ganymede",  2, -7,  3);
        mo[3] = new moon("Callisto",  9, -8, -3); */
        
        /**
         * Puzzle
         */
        mo[0] = new moon("Io",       -6,  2, -9);
        mo[1] = new moon("Europa",   12,-14, -4);
        mo[2] = new moon("Ganymede",  9,  5, -6);
        mo[3] = new moon("Callisto", -1, -4,  9); 

        print(0, mo);

        long steps = 0;
        int initPos = 0, initAxisX=0, initAxisY=0, initAxisZ=0;

        // Schleife so lange, bis alle Monde wieder an ihrer Ausgangsposition sind
        do {
            // Verarbeitet eine Zeit-Stufe (time)
            stepTime(mo);
            steps++;
            // Prüfung, ob alle Monde ihre Ausgangsposition wieder erreicht haben (dann initPos = Anzahl Monde)
            initPos = 0;
            for (int i=0; i<mo.length; i++) {
                initPos += (mo[i].initPos() ? 1 : 0);
            }
            // Ausgabe, sobald alle Monde ihre Ausgangsposition wieder habe
            if (initPos==mo.length) {
                System.out.println("It takes " + steps + " steps before they exactly match a previous point in time"); 
                print(steps, mo);
            // Ausgabe, wenn nur ein Mond seine Ausgangsposition wieder erreicht hat
            } else if (initPos>0) {
                System.out.println("On " + steps + " steps one moon is on its initial position"); 
                print(steps, mo);
            // Ausgabe alle x-Schritte
            } else if (steps % 1000 == 0) {
                //print(steps, mo);
                //System.out.println("x=" + initAxisX + "  y=" + initAxisY + "  z=" + initAxisZ); 

            }
            
            // Prüfen ob eine der Achsen wieder über alle Monde ihre Ausgangswerte haben und Anzahl Steps merken
            if (initAxisX == 0 && sameOnAxis(mo,'x')) {    initAxisX = (int) steps;  print(steps, mo); }
            if (initAxisY == 0 && sameOnAxis(mo,'y')) {    initAxisY = (int) steps;  print(steps, mo); }
            if (initAxisZ == 0 && sameOnAxis(mo,'z')) {    initAxisZ = (int) steps;  print(steps, mo); }

        } while (initAxisX==0 || initAxisY==0 || initAxisZ==0);

        // Meldung, dass alle Achsen-Ausgangs-Anzahl-Stufen ermitteln wurden
        System.out.println("All axis-back-inital-steps are calculatet after " + steps + ":");
        System.out.println("x=" + initAxisX + "  y=" + initAxisY + "  z=" + initAxisZ); 

        // Am Schluss nochmals Daten der Monde ausgeben
        //print(steps, mo);
        System.out.println("");
        System.out.println("It takes " + lcm(initAxisX, initAxisY, initAxisZ) + " steps before all moons are on its inital positions");

//391,807,628

        // Berechnung und Ausgabe der Gesamt-Energiemenge (unnütz für Part Two)
        //System.out.println("Total energy in the system: " + totalEnergy(mo));

        System.out.println("");
        System.out.println("ready.");
    }
    
    /**
     * stepTime
     * 
     * Verarbeitet eine Zeit-Stufe (time) und verändert erst die Velocity und 
     * anschließend die Positionen
     * 
     * @param moon[]        mo      Liste der Mond-Objekte
     */
    private static void stepTime(moon[] mo) {
        // Schleife je Mond über alle Monde, um Velocity (Geschwindigkeit) je Mond zu berechnen
        for (int m=0; m<mo.length; m++) {
            for (int v=0; v<mo.length; v++) {
                // nicht eigenen berechnen
                if (m!=v) {
                    mo[m].velX += (mo[m].posX==mo[v].posX ? 0 : (mo[m].posX>mo[v].posX ? -1 : 1));
                    mo[m].velY += (mo[m].posY==mo[v].posY ? 0 : (mo[m].posY>mo[v].posY ? -1 : 1));
                    mo[m].velZ += (mo[m].posZ==mo[v].posZ ? 0 : (mo[m].posZ>mo[v].posZ ? -1 : 1));
                }
            }
        }
        // Schleife über alle Monde, um Velocity auf die Positionen anzuwenden
        for (int m=0; m<mo.length; m++) {
            mo[m].posX += mo[m].velX;
            mo[m].posY += mo[m].velY;
            mo[m].posZ += mo[m].velZ;
        }       
    }
    
    /**
     * Passt die Strings, bzw. Zahlen der Länger nach rechts/links-bündig an,
     * um tabellarischen Ausdruck zu ermöglichen
     * 
     * @param   String  val
     * @return  String
     */
    private static String l10(String val) {
        val = val + "          ";
        return val.substring(0, 10);
    }
    private static String r4(int val) { return right(String.valueOf(val), 3); }
    private static String r6(int val) { return right(String.valueOf(val), 6); }
    private static String right(String val, int len) {
        val = "          " + val;
        return val.substring(val.length() - len);
    }
    
    /**
     * Gibt über die Konsole die Werte aller Monde in tabellarischer Form aus
     * 
     * @param long      step        Anzahl der Durchläufe für Andruck Zähler
     * @param moon[]    mo          Liste der Mond-Objekte
     */
    private static void print(long step, moon[] mo) {
        System.out.println("After "+step+" steps:");
        for (int i=0; i<mo.length; i++) {
            System.out.print("["+i+"] "+l10(mo[i].name));
            System.out.print("Pos="+r4(mo[i].posX)+"|"+r4(mo[i].posY)+"|"+r4(mo[i].posZ)+"  ");
            System.out.print("Vel="+r4(mo[i].velX)+"|"+r4(mo[i].velY)+"|"+r4(mo[i].velZ)+"   ");
            System.out.println("Pot="+r6(mo[i].pot())+"   Kin="+r6(mo[i].kin())+"   Total="+r6(mo[i].total()));
        }
        System.out.println("");
    }
    
    /**
     * Summiert alle Energie-Werte der Monde und gibt diese zurück.
     * 
     * @param   moon[]      Liste der Mond-Objekte
     * @return  int         Gesamt-Energiemenge aller Monde
     */
    private static int totalEnergy(moon[] mo) {
        int te = 0;
        for (int i=0; i<mo.length; i++) {
            te += mo[i].total();
        }
        return te;
    }
    
    /**
     * Größter, gemeinsamer Divisor ermittel  (greatest common divisor)
     * Bspw: 12 und 8 -> 4
     * 
     * @param   int     Wert 1
     * @param   int     Wert 2
     */
    private static long gcd(long a, long b) {
        if (b==0) { return a; }
        return gcd(b, a%b);
    }
    
    /**
     * Prüfung, ob eine der Achsen bei allen Monden wieder auf der Ausgangs-Position ist
     * 
     * @param   moon[]      Liste der Mond-Objekte
     * @param   char        zu prüfende Achse (x,y,z)
     * @return  boolen      Ist Achse (x,y,z) (Position und Velocity) mit Ausgangsposition identisch
     */
    private static boolean sameOnAxis(moon[] mo, char axis) {
        boolean x=true, y=true, z=true;
        for (int i = 1; i < mo.length; i++) {
            switch (axis) {
                case 'x':
                    if (mo[i].posX!=mo[i].initPosX || mo[i].velX!=mo[i].initVelX) {    return false;    }
                    break;
                case 'y':
                    if (mo[i].posY!=mo[i].initPosY || mo[i].velY!=mo[i].initVelY) {    return false;    }
                    break;
                case 'z':
                    if (mo[i].posZ!=mo[i].initPosZ || mo[i].velZ!=mo[i].initVelZ) {    return false;    }
                    break;
            }
        }
        return true;
    }
    
    /**
     * lowest common multiple
     * 
     * @param   int     Zähler X
     * @param   int     Zähler Y
     * @param   int     Zähler Z
     * @return  long    Rechenergebnis, wann alle Monde wieder auf ihrer Initialposition
     */
     private static long lcm(long x, long y, long z) {
         long rVal = x;
         rVal = (rVal * x) / gcd(rVal, x);
         rVal = (rVal * y) / gcd(rVal, y);
         rVal = (rVal * z) / gcd(rVal, z);
         return rVal;
     }
}



class moon{
    public String name;
    public int posX;
    public int posY;
    public int posZ;
    public int initPosX;
    public int initPosY;
    public int initPosZ;
    public int velX = 0;
    public int velY = 0;
    public int velZ = 0;
    public int initVelX = 0;
    public int initVelY = 0;
    public int initVelZ = 0;
    
    public moon(String NameIn, int x, int y, int z) {
        name = NameIn;
        posX = x;
        posY = y;
        posZ = z;
        initPosX = x;
        initPosY = y;
        initPosZ = z;
    }
    public int pot(){
        return (posX<0?posX*-1:posX)+(posY<0?posY*-1:posY)+(posZ<0?posZ*-1:posZ);
    }
    
    public int kin(){
        return (velX<0?velX*-1:velX)+(velY<0?velY*-1:velY)+(velZ<0?velZ*-1:velZ);
    }
    
    public int total(){
        return pot()*kin();
    }
    
    public boolean initPos() {
        boolean pos = (posX==initPosX && posY==initPosY && posZ==initPosZ ? true : false);
        boolean vel = (velX==initVelX && velY==initVelY && velZ==initVelZ ? true : false);
        return (pos==true && vel==true ? true : false);
    }
}
