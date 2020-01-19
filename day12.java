

public class day12 {
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

        for (int i=1; i<=1000; i++) {
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
            for (int m=0; m<mo.length; m++) {
                mo[m].posX += mo[m].velX;
                mo[m].posY += mo[m].velY;
                mo[m].posZ += mo[m].velZ;
            }
            if (i%100==0) {
                print(i, mo);
            }
        }
        
        System.out.println("Total energy in the system: " + totalEnergy(mo));

        System.out.println("ready.");
    }
    
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
    private static void print(int step, moon[] mo) {
        System.out.println("After "+step+" steps:");
        for (int i=0; i<mo.length; i++) {
            System.out.print("["+i+"] "+l10(mo[i].name));
            System.out.print("Pos="+r4(mo[i].posX)+"|"+r4(mo[i].posY)+"|"+r4(mo[i].posZ)+"  ");
            System.out.print("Vel="+r4(mo[i].velX)+"|"+r4(mo[i].velY)+"|"+r4(mo[i].velZ)+"   ");
            System.out.println("Pot="+r6(mo[i].pot())+"   Kin="+r6(mo[i].kin())+"   Total="+r6(mo[i].total()));
        }
        System.out.println("");
    }
    private static int totalEnergy(moon[] mo) {
        int te = 0;
        for (int i=0; i<mo.length; i++) {
            te += mo[i].total();
        }
        return te;
    }
}



class moon{
    public String name;
    public int posX;
    public int posY;
    public int posZ;
    public int velX = 0;
    public int velY = 0;
    public int velZ = 0;
    
    public moon(String NameIn, int x, int y, int z) {
        name = NameIn;
        posX = x;
        posY = y;
        posZ = z;
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
    
}
