import java.util.*;
import java.io.*;
import java.util.Map.*;

public class Main {
    // CodeTree - 단어장
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        // 값을 저장할 map 선언
        TreeMap<String, Integer> map = new TreeMap<>();
        for(int i = 0; i < N; i++){
            // 키 값 입력
            String key = br.readLine();
            // 키가 존재한다면, 기존 값을 가져온 뒤, 1을 더하고 다시 map에 입력
            if(map.containsKey(key)) map.put(key, map.get(key)+1);
            // 키가 존재하지 않는다면, key값과 value를 1로해서 새로 map에 추가
            else map.put(key, 1);
        }

        //Iterator 선언
        Iterator<Entry<String, Integer>> it = map.entrySet().iterator();
        while(it.hasNext()){
            Entry<String, Integer> e = it.next();
            // 오름차 순으로 key value를 공백을 기준으로 저장
            sb.append(e.getKey()).append(" ").append(e.getValue()).append("\n");
        }

        // 전체 결과 출력
        System.out.println(sb.toString());
    }
}