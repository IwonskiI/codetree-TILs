import java.util.*;
import java.util.Map.*;
import java.io.*;

public class Main {
    // CodeTree - 처음 등장하는 위치
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        TreeMap<Integer, Integer> map = new TreeMap<>();
        for(int i = 1; i <= N; i++){
            int key = Integer.parseInt(st.nextToken());
            // key값이 map에 없다면 현재 index와 함께 저장
            if(!map.containsKey(key)){
                map.put(key, i);
            }
            // key값이 map에 있다면 스킵
            else continue;
        }

        // Iterator 생성
        Iterator<Entry<Integer, Integer>> it = map.entrySet().iterator();
        while(it.hasNext()){
            // 오름차순으로 가져온 후 저장
            Entry<Integer, Integer> e = it.next();
            sb.append(e.getKey()).append(" ").append(e.getValue()).append("\n");
        }

        // 전체 저장 결과 출력
        System.out.println(sb.toString());
    }
}