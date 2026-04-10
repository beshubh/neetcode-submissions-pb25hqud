impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut prefix_max = vec![0; height.len()];
        let mut suffix_max = vec![0; height.len()];

        prefix_max[0] = 0;
        suffix_max[height.len() - 1] = height.len() - 1;

        for i in 1..height.len() {
            if height[i] > height[prefix_max[i - 1]] {
                prefix_max[i] = i;
            } else {
                prefix_max[i] = prefix_max[i - 1];
            }
        }
        for i in (0..(height.len() - 1)).rev() {
            if height[i] > height[suffix_max[i + 1]] {
                suffix_max[i] = i;
            } else {
                suffix_max[i] = suffix_max[i + 1];
            }
        }
        println!("prefix: {prefix_max:?}\nsuffix_max: {suffix_max:?}");
        let mut output = vec![0; height.len()];
        for i in 0..height.len() {
            output[i] = height[prefix_max[i]].min(height[suffix_max[i]]) - height[i];
        }
        println!("output: {output:?}");
        output.iter().sum()
    }
}
