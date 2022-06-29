def prime_factorize(n)
    r = []
    p = 2
    while n >= p*p
        if n%p==0
            r.append(p)
            n/=p
        else
            p+=1
        end
    end
    r.append(n)
    return r
end

def is_palindrome(n)
    s = n.to_s
    return s == s.reverse
end

def is_prime(n)
    if n == 1
        return false
    end
    i = 2
    while i*i <= n
        if n%i == 0
            return false
        end
        i += 1
    end
    return true
end

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

def solve003
    return prime_factorize(600851475143)[-1]
end

def solve004
    m = 0
    for i in (999).downto(100) do
        for j in (i).downto(100) do
            ml = i*j
            if is_palindrome(ml) and ml > m then
                m = ml
            end
        end
    end
    return m
end

def solve006
    n1 = 0
    n2 = 0
    for i in (1..100).to_a do
        n1 += i*i
        n2 += i
    end
    n2 *= n2
    return n2 - n1
end

def solve007
    i = 3
    p = [2]
    while p.length() != 10001
        if is_prime(i)
            p.push(i)
        end
        i += 2
    end
    return p[10000]
end

def main
    case ARGV[0]
    when "1"
        puts solve001
    when "2"
        puts solve002
    when "3"
        puts solve003
    when "4"
        puts solve004
    when "6"
        puts solve006
    when "7"
        puts solve007
    else
        puts "NA"
    end
end

main