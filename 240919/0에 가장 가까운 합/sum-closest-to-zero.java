import java.io.*;
import java.util.*;

public class Main {
    
	// CodeTree - 0에 가장 가까운 합
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        
        int N = Integer.parseInt(br.readLine());
        int[] lst = new int[N];
        st = new StringTokenizer(br.readLine());
        
        // 초기 입력
        for(int i = 0; i < N; i++) {
        	lst[i] = Integer.parseInt(st.nextToken());
        }
        // 오름차순 출력을 위한 정렬
        Arrays.sort(lst);
        
        int sp = 0, ep = N - 1;
        int min = Integer.MAX_VALUE;
        
        while(min > 0) {
        	int sum = lst[sp] + lst[ep];
        	
        	if(sum > 0) ep--;
        	else if(sum < 0) sp++;

            if(sp == ep) break;
        	
        	min = Math.min(Math.abs(sum), min);
        }
        
        
        // 정답 저장
        sb.append(min);
        
        // 최종 결과 출력
        System.out.println(sb.toString());
    }
}