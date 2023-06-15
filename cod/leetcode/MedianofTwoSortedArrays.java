package corejava;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
public class MedianofTwoSortedArrays {

	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt(); // số truy vấn
        Queue<Integer> queue = new LinkedList<>(); // khởi tạo hàng đợi rỗng

        for (int i = 0; i < n; i++) {
            int queryType = input.nextInt(); // loại truy vấn

            switch (queryType) {
                case 1:
                    int x = input.nextInt(); // giá trị cần đưa vào hàng đợi
                    queue.add(x); // đưa vào cuối hàng đợi
                    break;
                case 2:
                    if (!queue.isEmpty()) {
                        queue.remove(); // loại bỏ phần tử ở đầu hàng đợi
                    }
                    break;
                case 3:
                    if (!queue.isEmpty()) {
                        System.out.println(queue.peek()); // in ra phần tử ở đầu hàng đợi
                    } else {
                        System.out.println("Empty!"); // nếu hàng đợi rỗng thì in ra Empty!
                    }
                    break;
                   
            }
        }

        input.close(); // đóng scanner
    }
	

}
