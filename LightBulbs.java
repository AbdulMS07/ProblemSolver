public class LightBulbs{
    public static void main(String[] args){
        int[] lights = new int[101];
        for(int i = 1; i <= 101;i++){
            for(int j = i;j < lights.length;j+=i){
                lights[j] = lights[j] == 1 ? 0 : 1;
            }
        }
        int counter = 0;
        for(int i = 1; i < lights.length;i++){
            if(lights[i]==1) counter++;
            System.out.println(String.format("Bulb Number: %d --- State = %s",i,lights[i]==1?"ON":"OFF"));
        }
        System.out.println("Total Number of Bulbs in ON state is: "+counter);
    }
}

// To find more details about the problem -> https://puzzles.nigelcoldwell.co.uk/six.htm
