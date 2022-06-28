def solve001
    return (1...1000).to_a.map{ |i| if i%3 == 0 or i % 5 == 0 then i else 0 end}.sum
end

def solve002
    fib = [1, 2]
    while fib[-1] < 4000000
        fib.push(fib[-1]+fib[-2])
    end
    fib.pop()
    s = 0
    fib.each{|i| if i%2 == 0 then s+=i end}
    return s
end

def main
    case ARGV[0]
    when "1"
        puts solve001
    when "2"
        puts solve002
    else
        puts "NA"
    end
end

main