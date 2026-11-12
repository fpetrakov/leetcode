class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        const chars = {};

        for (let ch of s1) {
            chars[ch] = (chars[ch] || 0) + 1;
        }

        for (let i = 0; i < s2.length; i++) {
            const curr = s2[i];
            if (chars[curr] === undefined) continue;

            let j = i + 1;
            const counter = { ...chars };
            counter[curr] -= 1;

            while (j - i !== s1.length) {
                const ch = s2[j];
                if (counter[ch] === undefined || counter[ch] <= 0) break;

                counter[ch] -= 1;
                j += 1;
            }

            if (j - i === s1.length) return true;
        }

        return false;
    }
}
