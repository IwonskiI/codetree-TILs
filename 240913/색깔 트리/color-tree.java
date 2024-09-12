import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int Q;
    public static StringBuilder sb = new StringBuilder();
    
    public static int scores;
    public static int[] colors = new int[100001], parents = new int[100001];
    public static int[] mds = new int[100001], cds = new int[100001];
//    public static int[][] scores = new int[100001][5];
    public static boolean[] c_lst;
    public static List<Integer> root = new LinkedList<>();
    public static TreeMap<Integer, List<Integer>> child = new TreeMap<>();
    
    public static void dfs(int i) {
    	boolean[] c_old = new boolean[5];
    	for(int ch : child.getOrDefault(i, new ArrayList<>())) {
    		dfs(ch);
    		for(int dd = 0; dd < 5; dd++) {
    			c_old[dd] |= c_lst[dd];
    		}
    		c_lst = new boolean[5];
    	}
    	c_old[colors[i]-1] = true;
    	int cnt = 0;
    	for(int dd = 0; dd < 5; dd++) {
    		if(c_old[dd]) cnt++;
    	}
    	for(int dd = 0; dd < 5; dd++) {
    		c_lst[dd] = c_old[dd];
    	}
    	scores += (cnt * cnt);
    }
    
    public static void add(int mid, int pid, int color, int md) {
    	if(pid == -1) {
    		root.add(mid);
    	}
    	else {
    		if(mds[pid] == 1) return;
    		if(mds[pid] - 1 < md) md = mds[pid] - 1;
    		child.computeIfAbsent(pid, v -> new ArrayList<>()).add(mid);
    	}
    	mds[mid] = md;
    	parents[mid] = pid;
    	colors[mid] = color;
    	
    	return;
    }
    
    public static void change(int mid, int color) {
    	Queue<Integer> c_q = new LinkedList<>();
    	c_q.offer(mid);
    	while(!c_q.isEmpty()) {
    		int cur = c_q.poll();
    		for(int k : child.getOrDefault(cur, new ArrayList<>())) {
    			c_q.offer(k);
    		}
    		colors[cur] = color;
    	}
    	return;
    }
    
    public static void search(int mid) {
    	sb.append(colors[mid]).append("\n");
    	
    	return;
    }
    
    public static void calc() {
    	scores = 0;
    	for(int i : root) {
    		c_lst = new boolean[5];
    		dfs(i);
    	}
    	sb.append(scores).append("\n");
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        // 입력:
        Q = Integer.parseInt(br.readLine());
        for(int i = 0; i < Q; i++) {
        	st = new StringTokenizer(br.readLine());
            int cmd = -1;
            int mid = -1, pid = -1, color = -1, md = -1;
            cmd = Integer.parseInt(st.nextToken());
            if(cmd == 100) {
                mid = Integer.parseInt(st.nextToken());
                pid = Integer.parseInt(st.nextToken());
                color = Integer.parseInt(st.nextToken());
                md = Integer.parseInt(st.nextToken());
                add(mid, pid, color, md);
            }
            else if(cmd == 200) {
                mid = Integer.parseInt(st.nextToken());
                color = Integer.parseInt(st.nextToken());
                change(mid, color);
            } 
            else if(cmd == 300) {
                mid = Integer.parseInt(st.nextToken());
                search(mid);
            }
            else if(cmd == 400) {
            	calc();
            }
        }
        
        System.out.println(sb.toString());
    }
}