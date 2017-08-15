class Test {
    public static int returnFirstMatchIndex(int[] array, int query) {
        int ret = -1;
        for (int i = 0; i < array.length; i++) {
            if (array[i] == query) {
                return i;
            }
        }
        return ret;
    }
    
    public static int returnNumberOfMatches(int[] array, int query) {
        int count = 0;
        for (int item : array) {
            if (item == query) {
                count++;
            }
        }
        return count;
    }
    
    public static void main(String[] args) {
        int[] values = {0,1,2,3,4,4,5,6,7,8,8,8,9};
        //System.out.println(values.length);
        System.out.println(returnFirstMatchIndex(values, 8));
        System.out.println(returnNumberOfMatches(values, 8));
        
    }
}