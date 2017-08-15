class Gravity {
    public static double[] computePosition(double a0x , double v0x, double v0y, double x0, double y0, double t) {
        /* ay = -g
         * v_y(t) = a * t + v0y
         * y(t) = .5 * a * t * t + v0 * t + y0
         * 
         * ax = a0x
         * v_x(t) = a0x * t + v0x
         * x(t) = .5 * a0x * t * t + v0x * t + x0
         * 
         * 
         */
        double x = .5 * a0x * t * t + v0x * t + x0;
        double y = .5 * -9.8 * t * t + v0x * t + y0;
        double[] ret = {x,y};
        return ret;
    }
    
    public static void main (String[] args) {
        double[] times = {0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
        for (double t : times)  {  
            System.out.println("time: " + t);
            double[] answer = computePosition(0,0,0,0,10,t);
            for (double item : answer) {
                System.out.println(item);
            }
            System.out.println();
        }
    }
}