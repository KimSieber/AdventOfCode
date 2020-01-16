public class sortieren {
    public static void main(String args[]){
        tools tl = new tools();
    	double[][] unsortiert={{1,5,0},
    	                    {2,5,0},
    	                    {1,2,0},
    	                    {4,2,0},
    	                    {8,9,0}};
    	double[][] kalkuliert = tl.calcDivisor(unsortiert);
    	double[][] sortiert=tl.bubblesort(kalkuliert,2);
    	
    	for (int i=0; i<sortiert.length; i++) {
    		System.out.print((int)sortiert[i][1] + " / ");
    		System.out.print((int)sortiert[i][0] + " = ");
    		System.out.print(sortiert[i][2]);
        	System.out.println("");
    	}
    }
}

class tools {
    
    public double[][] calcDivisor(double[][] Map) {
        for (int i=0; i<Map.length; i++) {
            Map[i][2] = Map[i][1] / Map[i][0];
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
}
