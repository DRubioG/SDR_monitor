library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use std.textio.all;
use ieee.std_logic_textio.all;
use ieee.numeric_std.all;

entity I_Q_top_tb is
end I_Q_top_tb;

architecture Behavioral of I_Q_top_tb is
component I_Q_top is
    generic(
        WIDTH : integer := 8
    );
    Port ( 
        clk : in std_logic;
        rst_n : in std_logic;
        com_signal : out std_logic_vector(WIDTH-1 downto 0);
        clk_com : out std_logic
    );
end component;

constant WIDTH : integer := 8;
signal clk :  std_logic:='0';
signal rst_n :  std_logic;
signal com_signal :  std_logic_vector(WIDTH-1 downto 0);
signal clk_com :  std_logic;

file fichero_salida : text open write_mode is "datos_out.dat";
signal end_sim : std_logic:='0';
signal cont : unsigned(31 downto 0) := (others=>'0');

begin

DUT : I_Q_top 
    generic map(
        WIDTH => WIDTH
    )
    Port map( 
        clk => clk,
        rst_n => rst_n,
        com_signal => com_signal,
        clk_com => clk_com
    );
    
    clk <= not clk after 5ns;
    rst_n <= '0', '1' after 50ns; 


    process
        variable linea_salida : line;
    begin
        while end_sim = '0' loop
            wait until rising_edge(clk);
            write(linea_salida, com_signal);
            writeline(fichero_salida, linea_salida);
            cont <= cont+1;
            if cont > x"000FFFF0" then
                end_sim <= '1';
            end if;
            
        end loop;
        file_close(fichero_salida);
        report " FIN DE LA SIMULACION" severity failure;
     end process;
     
     

end Behavioral;
