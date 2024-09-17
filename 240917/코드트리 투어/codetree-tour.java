import java.io.*;
import java.util.*;

public class Main {
    
    // CodeTree - 코드트리 투어
	public static StringBuilder sb = new StringBuilder();
	public static StringTokenizer st;
	public static int N, M;
	public static int[][] path;
	public static int[] cost;
	public static boolean[] is_sell = new boolean[30010];
	public static PriorityQueue<int[]> p_lst = new PriorityQueue<>((a, b) -> {
		if(a[3] == b[3]) return a[0] - b[0];
		return b[3] - a[3];
	});
	
	public static void dijkstra(int sv) {
		PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) ->{
			if(a[1] == b[1]) return a[0] - b[0];
			return a[1] - b[1];
		});
		pq.offer(new int[] {sv, 0});
		cost[sv] = 0;
		
		while(!pq.isEmpty()) {
			int[] cur = pq.poll();
			int cv = cur[0], dist = cur[1];
			if(cost[cv] < dist) continue;
			for(int i = 0; i < N; i++) {
				if(path[cv][i] == 200) continue;
				int nextDist = dist + path[cv][i];
				
				if(nextDist < cost[i]) {
					cost[i] = nextDist;
					pq.offer(new int[] {i, nextDist});
				}
			}
		}
	}
	
	public static void init() {
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		path = new int[N][N];
		cost = new int[N];
		Arrays.fill(cost, 200);
		for(int i = 0; i < N; i++) {
			Arrays.fill(path[i], 200);
			path[i][i] = 0;
		}
		
		for(int i = 0; i < M; i++) {
			int v = Integer.parseInt(st.nextToken());
			int u = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			if(v == u) continue;
			path[u][v] = Math.min(path[u][v], w);
			path[v][u] = Math.min(path[v][u], w);
		}
		
		dijkstra(0);
	}
	
	public static void create() {
		int id = Integer.parseInt(st.nextToken());
		int rv = Integer.parseInt(st.nextToken());
		int d_id = Integer.parseInt(st.nextToken());
		int profit = rv-cost[d_id] < 0 ? -1 : rv - cost[d_id];
		
		p_lst.offer(new int[] {id, rv, d_id, profit});
		is_sell[id] = true;
	}
	
	public static void cancel() {
		int id = Integer.parseInt(st.nextToken());
		is_sell[id] = false;
	}
	
	public static void sell() {
		int ans = -1;
        // 큐에서 취소되거나 수익이 음수인 상품을 제거
        while(!p_lst.isEmpty()) {
            int[] cur = p_lst.peek();
            // 상품이 취소되었거나 수익이 음수면 큐에서 제거
            if(!is_sell[cur[0]] || cur[3] < 0) {
                p_lst.poll(); // 제거
            } else {
                ans = cur[0];
                p_lst.poll(); // 판매된 상품 제거
                break;
            }
        }
		sb.append(ans).append("\n");
//		while(!p_lst.isEmpty() && !is_sell[p_lst.peek()[0]]) {
//			p_lst.poll();
//		}
//		if(p_lst.isEmpty()) sb.append("-1\n");
//		else {
//			int[] cur = p_lst.peek();
//			if(cur[3] < 0) sb.append("-1\n");
//			else {
//				cur = p_lst.poll();
//				sb.append(cur[0]).append("\n");
//			}
//		}
	}
	
	public static void change() {
		cost = new int[N];
		Arrays.fill(cost, 200);
		dijkstra(Integer.parseInt(st.nextToken()));
		
		PriorityQueue<int[]> temp_pq = new PriorityQueue<>((a, b) -> {
			if(a[3] == b[3]) return a[0] - b[0];
			return b[3] - a[3];
		});
		
		while(!p_lst.isEmpty()) {
			int[] cur = p_lst.poll();
			int profit = cur[1]-cost[cur[2]] < 0 ? -1 : cur[1] - cost[cur[2]];
			temp_pq.offer(new int[] {cur[0], cur[1], cur[2], profit});
		}
		
		p_lst = temp_pq;
	}
	
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int Q = Integer.parseInt(br.readLine());
        
        for(int q = 0; q < Q; q++) {
        	st  = new StringTokenizer(br.readLine());
        	
        	int mod = Integer.parseInt(st.nextToken());
        	
        	switch(mod) {
        	case 100:
        		init();
        		break;
        	case 200:
        		create();
        		break;
        	case 300:
        		cancel();
        		break;
        	case 400:
        		sell();
        		break;
        	case 500:
        		change();
        		break;
        	}
        }
        
        // 최종 결과 출력
        System.out.println(sb.toString());
    }

}