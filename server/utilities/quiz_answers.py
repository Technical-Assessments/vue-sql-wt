

# 1. Obtener la cantidad de empleados por género de cada departamento.
query_1 = """
        SELECT dep.dept_name, em.gender, COUNT(DISTINCT em.emp_no) as total
        FROM employees.employees em
        INNER JOIN employees.dept_emp mtm ON em.emp_no = mtm.emp_no
        INNER JOIN employees.departments dep ON mtm.dept_no = dep.dept_no
        GROUP BY dep.dept_name, em.gender
        """

# 2. Obtén los nombres de los managers activos y el de su predecesor por cada departamento.
query_2 = """
        SELECT main.dept_name, main.manager, main.predecessor
        FROM (
            SELECT dep.dept_no, dep.dept_name, tt.title, tt.from_date, tt.to_date, CONCAT(em.first_name, ' ', em.last_name) AS manager,
            LAG(CONCAT(em.first_name, ' ', em.last_name), 1) OVER (
                PARTITION BY dep.dept_no
                ORDER BY tt.from_date ASC) as predecessor
            FROM employees.departments dep
            INNER JOIN employees.dept_manager dm
                ON dep.dept_no = dm.dept_no
            INNER JOIN employees.titles tt
                ON dm.emp_no = tt.emp_no
            INNER JOIN employees.employees em
                ON tt.emp_no = em.emp_no
            WHERE tt.title LIKE 'Manager'
            ORDER BY dep.dept_name, tt.to_date DESC) AS main
        WHERE main.to_date > now()
        """

# 3. Obtén la cantidad de empleados que tiene cada manager.

query_3 = """
        SELECT managers.manager, non_managers.staff_count
        FROM (
        -- Mangers
            SELECT
                em.emp_no,
                CONCAT(em.first_name, ' ', em.last_name) AS manager,
                t.title, d.dept_no
            FROM employees em
            INNER JOIN titles t ON em.emp_no = t.emp_no
            INNER JOIN dept_manager dm on em.emp_no = dm.emp_no 
            INNER JOIN departments d on dm.dept_no = d.dept_no
            WHERE t.title LIKE 'Manager'
            ORDER BY d.dept_name
            ) AS managers

        JOIN
            (
        -- Non-Manager employees / dept
            SELECT d.dept_no, COUNT(DISTINCT em.emp_no) - 1 staff_count
            FROM employees em
            INNER JOIN titles t ON em.emp_no = t.emp_no
            INNER JOIN dept_manager dm on em.emp_no = dm.emp_no 
            INNER JOIN departments d on dm.dept_no = d.dept_no
            WHERE t.title != 'Manager'
            GROUP BY d.dept_name	
            ) AS non_managers
            
        ON managers.dept_no = non_managers.dept_no
        """
    
# 4. Obtén un listado de los empleados con mayor ingreso y con el menor ingreso por cada departamento.
query_4 = """
        SELECT 
        d.dept_name , MAX(s.salary) max_salary , MIN(s.salary) min_salary
        FROM departments d
        INNER JOIN dept_emp de ON d.dept_no = de.dept_no
        INNER JOIN employees e ON de.emp_no = e.emp_no 
        INNER JOIN salaries s ON e.emp_no = s.emp_no 

        GROUP BY d.dept_no
        """

# 5. Obtén un listado de todos los cargos con la cantidad de empleados y a su vez mostrar el empleado más antiguo y el más nuevo.
query_5 = """
        
        """