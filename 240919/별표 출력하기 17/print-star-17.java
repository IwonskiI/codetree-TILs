import java.io.*;

public class Main {
    
	// CodeTree - 별표 출력하기 17
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        // N 입력
        int N = Integer.parseInt(br.readLine());
        
        for(int i = 1; i < N; i++) {
        	for(int j = 0; j < i; j++) {
        		sb.append("*");
        	}
        	sb.append("\n");
        }
        for(int i = N; i > 0; i--) {
        	for(int j = 0; j < i; j++) {
        		sb.append("*");
        	}
        	sb.append("\n");
        }
                
        // 최종 결과 출력
        System.out.println(sb.toString());
    }
}