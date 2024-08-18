library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.numeric_std.all;

entity I_Q_top is
    generic(
        WIDTH : integer := 8
    );
    Port ( 
        clk : in std_logic;
        rst_n : in std_logic;
        com_signal : out std_logic_vector(WIDTH-1 downto 0);
        clk_com : out std_logic
    );
end I_Q_top;

architecture Behavioral of I_Q_top is


component I_Q_signal is
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
end component;

signal Q_signal : std_logic_vector(WIDTH-1 downto 0);
signal I_signal : std_logic_vector(WIDTH-1 downto 0);

begin


impl_I_Q_signal : I_Q_signal
    port map(
        clk => clk,
        rst => rst_n,
        Q_out => Q_signal,
        I_out => I_signal
    );
    
    com_signal <= std_logic_vector(unsigned(Q_signal) - unsigned(I_signal));

end Behavioral;
