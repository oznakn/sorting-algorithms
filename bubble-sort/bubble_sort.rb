def bubble_sort(array)		
	loop do
		sorted = false
		(array.length-1).times do |i|	
			if array[i] > array[i+1] 				
				array[i], array[i+1] = array[i+1], array[i] 
				sorted = true
			end	
		end
		break if not sorted
	end
	array
end

arr = *(1..100)
arr = arr.shuffle
puts "before: ", arr
puts "after: ", bubble_sort(arr)