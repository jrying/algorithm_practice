import java.util.*;

public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> m = new LinkedHashMap<Integer, Integer>();
        List<Integer> l = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (m.get(nums[i]) != null) {
                m.put(nums[i], m.get(nums[i]) + 1);
            }
            else {
                m.put(nums[i], 1);
            }
        }
        m.entrySet().stream()
            .sorted(Collections.reverseOrder(Map.Entry.comparingByValue()))
            .limit(k)
            //.forEach(System.out::println);
            .forEachOrdered(e -> l.add(e.getKey()));
        return l;
    }
}
