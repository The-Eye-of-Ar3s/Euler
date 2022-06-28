def solve001
    return (1...1000).to_a.map{ |i| if i%3 == 0 or i % 5 == 0 then i else 0 end}.sum
end

def main
    case ARGV[0]
    when "1"
        puts solve001
    else
        puts "NA"
    end
end

main