import java.io.*;

public class Main {
    
	// CodeTree - 효율적으로 분배하기
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        // N 입력
        int N = Integer.parseInt(br.readLine());
        
        // 최대한 많은 수를 담아야하므로 일단 5로 최대한 담아봄
        int five = N / 5, left = N % 5;
        int ans = -1;
        
        // 나머지에 따라서 3 상자 개수 정하기
        switch(left) {
        // 나눠 떨어지면 5로만 담는게 최소 상자
        case 0:
        	ans = five;
        	break;
        // 나머지가 1이라면 5상자 한개 빼고 3상자 2개로 나눠 떨어짐 (-1 + 2 = 1)
        case 1:
        	// 5 상자가 1개 이상이라면 계산
        	if(five >= 1) ans = five + 1;
        	// 아니라면 ans의 초기값 -1 그대로 종료
        	break;
        // 나머지가 2라면 5상자 두 개 빼고 3상자 4개로 나눠 떨어짐 (-2 + 4 = 2)
        case 2:
        	// 5 상자가 2개 이상이라면 계산
        	if(five >= 2) ans = five + 2;
        	// 아니라면 ans의 초기값 -1 그대로 종료
        	break;
        // 나머지가 3이라면 3상자 한개만 더하면 나눠 떨어짐
        case 3:
        	ans = five + 1;
        	break;
        // 나머지가 4라면 5상자 한 개 빼고 3상자 3개로 나눠 떨어짐 (-1 + 3 = 2)
        case 4:
        	// 5 상자가 1개 이상이라면 계산
        	if(five >= 1) ans = five + 2;
        	// 아니라면 ans의 초기값 -1 그대로 종료
        	break;
        }
        
        // 최종 결과 출력
        System.out.println(ans);
    }
}