library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;


entity I_Q_signal is
    generic(
            WIDTH : integer := 8;
            N : integer := 100
    );
    port(
        clk : in std_logic;
        rst : in std_logic;
        Q_out : out std_logic_vector(WIDTH-1 downto 0);
        I_out : out std_logic_vector(WIDTH-1 downto 0)
    );
end I_Q_signal;

architecture Behavioral of I_Q_signal is

type seno_array is array (0 to N-1) of std_logic_vector(WIDTH-1 downto 0);

signal Q : seno_array := (x"80", x"88", x"90", x"98", x"a0",
                          x"a7", x"af", x"b7", x"be", x"c5", 
                          x"cb", x"d2", x"d8", x"de", x"e3", 
                          x"e8", x"ec", x"f0", x"f4", x"f7", 
                          x"fa", x"fc", x"fe", x"ff", x"ff", 
                          x"ff", x"ff", x"fe", x"fd", x"fb", 
                          x"f8", x"f6", x"f2", x"ee", x"ea", 
                          x"e5", x"e0", x"db", x"d5", x"cf", 
                          x"c8", x"c1", x"ba", x"b3", x"ab", 
                          x"a4", x"9c", x"94", x"8c", x"84", 
                          x"7b", x"73", x"6b", x"63", x"5b", 
                          x"54", x"4c", x"45", x"3e", x"37", 
                          x"30", x"2a", x"24", x"1f", x"1a", 
                          x"15", x"11", x"0d", x"09", x"07", 
                          x"04", x"02", x"01", x"00", x"00", 
                          x"00", x"00", x"01", x"03", x"05", 
                          x"08", x"0b", x"0f", x"13", x"17", 
                          x"1c", x"21", x"27", x"2d", x"34", 
                          x"3a", x"41", x"48", x"50", x"58", 
                          x"5f", x"67", x"6f", x"77", x"7f");

signal I : seno_array := (x"00", x"00", x"01", x"03", x"05", 
                          x"08", x"0b", x"0f", x"13", x"17", 
                          x"1c", x"21", x"27", x"2d", x"34", 
                          x"3a", x"41", x"48", x"50", x"58", 
                          x"5f", x"67", x"6f", x"77", x"7f",
                          x"80", x"88", x"90", x"98", x"a0",
                          x"a7", x"af", x"b7", x"be", x"c5", 
                          x"cb", x"d2", x"d8", x"de", x"e3", 
                          x"e8", x"ec", x"f0", x"f4", x"f7", 
                          x"fa", x"fc", x"fe", x"ff", x"ff", 
                          x"ff", x"ff", x"fe", x"fd", x"fb", 
                          x"f8", x"f6", x"f2", x"ee", x"ea", 
                          x"e5", x"e0", x"db", x"d5", x"cf", 
                          x"c8", x"c1", x"ba", x"b3", x"ab", 
                          x"a4", x"9c", x"94", x"8c", x"84", 
                          x"7b", x"73", x"6b", x"63", x"5b", 
                          x"54", x"4c", x"45", x"3e", x"37", 
                          x"30", x"2a", x"24", x"1f", x"1a", 
                          x"15", x"11", x"0d", x"09", x"07", 
                          x"04", x"02", x"01", x"00", x"00"
                          );

signal cont : integer range 0 to N-1;

begin

    process(clk, rst)
    begin
        if rst = '0' then
            cont <= 0;
        elsif rising_edge(clk) then
            
            if cont = N-1 then
                cont <= 0;
            else
                cont <= cont +1;
            end if;
        end if;
    end process;
    
    Q_out <= Q(cont);
    I_out <= I(cont);
    
end architecture;
