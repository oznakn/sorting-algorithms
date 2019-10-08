function Bogosort(arr){
    var is_sorted = function(arr){
        for(var i = 1; i < arr.length; i++){
            if (arr[i-1] > arr[i]) {
                return false;
            }
        }
        return true;
    };
    function shuffle(array) {
       array.sort(() => Math.random() - 0.5);
    }
   function sort(arr){
        var sorted = false;
        while(!sorted){
            shuffle(arr);
            sorted = is_sorted(arr);
        }
        return arr;
    }
    return sort(arr);
}
var array = [7, 5, 6, 3, 1, 2]; 
console.log(Bogosort(array));