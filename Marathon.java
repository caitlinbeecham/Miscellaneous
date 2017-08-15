class Marathon {
    
    public static int findFastestRunner(String[] names, int[] times) {
        int fastest_time = times[0];
        int fastest_time_index = 0;
        for (int i = 0; i < times.length; i++) {
            if (times[i] < fastest_time) {
                fastest_time = times[i];
                fastest_time_index = i;
            }
        }
        System.out.println(names[fastest_time_index]);
        System.out.println(times[fastest_time_index]);
        return fastest_time_index;
        
    }
    
    public static int findSecondFastestRunner(String[] names, int[] times, int fastest_time_index) {
        int fastest_time = times[fastest_time_index];
        int second_fastest_time = times[0];
        int second_fastest_time_index = 0;
        for (int i = 0; i < times.length; i++) {
            if ((times[i] < second_fastest_time) && (times[i] > fastest_time)) {
                second_fastest_time = times[i];
                second_fastest_time_index = i;
            }
        }
        System.out.println(names[second_fastest_time_index]);
        System.out.println(times[second_fastest_time_index]);
        return second_fastest_time_index;
    }
    
    public static void main (String[] arguments) {
        String[] names = {
            "Elena", "Thomas", "Hamilton", "Suzie", "Phil", "Matt", "Alex",
            "Emma", "John", "James", "Jane", "Emily", "Daniel", "Neda",
            "Aaron", "Kate"
        };

        int[] times = {
            341, 273, 278, 329, 445, 402, 388, 275, 243, 334, 412, 393, 299,
            343, 317, 265
        };

        for (int i = 0; i < names.length; i++) {
            System.out.println(names[i] + ": " + times[i]);
        }
        
        int fastest_time_index = findFastestRunner(names, times);
        findSecondFastestRunner(names, times, fastest_time_index);
    }
} 