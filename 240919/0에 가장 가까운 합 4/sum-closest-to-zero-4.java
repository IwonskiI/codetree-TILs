import java.io.*;
import java.util.*;

public class Main {
    
	// CodeTree - 0에 가장 가까운 합
	public static int N, min = Integer.MAX_VALUE;
	public static int[] lst, ans = new int[3], num = new int[3];
	public static boolean[] using;
	
	// 만들 수 있는 조합 계산
	public static void combi(int start, int cnt) {
		// 조합 완성됐다면
		if(cnt == 3) {
			// 현재 조합의 합 구하기
			int sum = 0;
			for(int i = 0; i < 3; i++) {
				sum += num[i];
			}
			// 현재 총 합의 절댓값이 기존 최소값보다 작다면(0에 더 가깝다면)
			if(Math.abs(sum) < min) {
				// ans배열 갱신
				for(int i = 0; i < 3; i++) {
					ans[i] = num[i];
				}
				// 최솟값 갱신
				min = Math.abs(sum);
			}
			return;
		}
		
		// 시작점부터 사용중이지 않는 숫자들로 조합 구성
		for(int i = start; i < N; i++) {
			// 사용중이라면 스킵
			if(using[i]) continue;
			// 현재 위치에 i번째 숫자를 입력
			num[cnt] = lst[i];
			// 사용중 표시
			using[i] = true;
			// 다음 자리 조합 계산
			combi(i+1, cnt+1);
			// 탐색 완료 후 사용중 표시 해제
			using[i] = false;
		}
	}
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        
        N = Integer.parseInt(br.readLine());
        lst = new int[N];
        using = new boolean[N];
        st = new StringTokenizer(br.readLine());
        
        // 초기 입력
        for(int i = 0; i < N; i++) {
        	lst[i] = Integer.parseInt(st.nextToken());
        }
        // 오름차순 출력을 위한 정렬
        Arrays.sort(lst);
        
        // 조합 계산
        combi(0, 0);
        
        // 정답 저장
        for(int i = 0; i < 3; i++) {
        	sb.append(ans[i]).append(" ");
        }
        
        // 최종 결과 출력
        System.out.println(sb.toString());
    }
}