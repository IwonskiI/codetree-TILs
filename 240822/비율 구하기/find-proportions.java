import java.util.*;
import java.util.Map.*;
import java.io.*;

public class Main {
    // CodeTree - 비율 구하기
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        // 각 값을 저장할 TreeMap
        TreeMap<String, Integer> map = new TreeMap<>();
        // 입력값의 개수
        int N = Integer.parseInt(br.readLine());
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            // key값이 될 문자열
            String color = st.nextToken();
            // map에 key값이 존재한다면,
            if(map.containsKey(color)){
                // 기존 값을 가져 온 뒤, 거기에 1을 더하고 다시 map에 입력
                map.put(color, map.get(color)+1);
            }
            // map에 key값이 없다면,
            else{
                // key값과 value는 1로 해서 map에 새로 추가
                map.put(color, 1);
            }
        }

        // Iterator 선언
        Iterator<Entry<String, Integer>> it = map.entrySet().iterator();

        while(it.hasNext()) {
            Entry<String, Integer> entry = it.next();
            // key값과 value의 비율을 계산해서 저장
            sb.append(entry.getKey()).append(" ").append(String.format("%.4f", (double)entry.getValue() / N * 100)).append("\n");
        }
        // 전체 결과 출력
        System.out.println(sb.toString());
    }
}