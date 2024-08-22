import java.util.*;
import java.util.Map.*;
import java.io.*;

public class Main {
    // CodeTree - treemap 기본
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        // TreeMap 선언
        TreeMap<Integer, Integer> treemap = new TreeMap<>();
        // 명령의 개수 N
        int N = Integer.parseInt(br.readLine());

        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            // 명령의 종류 op
            String op = st.nextToken();
            // 입력값 key, value
            int k, v;
            switch(op){
                // add 명령
                case "add":
                    k = Integer.parseInt(st.nextToken());
                    v = Integer.parseInt(st.nextToken());
                    // treemap에 추가
                    treemap.put(k, v);
                    break;
                // find 명령
                case "find":
                    k = Integer.parseInt(st.nextToken());
                    // key가 map에 있는지 먼저 확인
                    // map에 key가 있다면, 
                    if(treemap.containsKey(k)) {
                        // treemap에서 k를 key로 하는 값 가져오기
                        sb.append(treemap.get(k)).append("\n");
                    }
                    // map에 key가 없다면,
                    else {
                        // None 추가
                        sb.append("None\n");
                    }
                    break;          
                // print_list 명령        
                case "print_list":
                    // map이 비어있다면,
                    if(treemap.isEmpty()) {
                        // None 추가
                        sb.append("None\n");
                    }
                    // map에 요소가 있다면,
                    else {
                        // Iterator 생성
                        Iterator<Entry<Integer, Integer>> it = treemap.entrySet().iterator();
                        // Iterator에 다음 요소가 있을 때까지
                        while(it.hasNext()){
                            // Iterator의 요소는 Entry<K, V>형태
                            Entry<Integer, Integer> entry = it.next();
                            // Entry<K, V>에서 .getKey()로 key값을, .getValue()로 value값을 가져옴
                            // value만 공백을 기준으로 출력
                            sb.append(entry.getValue()).append(" ");
                        }
                        sb.append("\n");
                    }
                    break;
                // remove 명령
                case "remove":
                    k = Integer.parseInt(st.nextToken());
                    // 잘못된 명령이 없으므로 검증하지 않고 제거
                    // treemap에서 k를 key로 하는 값 제거
                    treemap.remove(k);
                    break;

            }
        }
        // 전체 결과 출력
        System.out.println(sb.toString());
    }
}