/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var a = 0;
    for (let num of nums) {
        a ^= num;
    }
    return a;
    
};
