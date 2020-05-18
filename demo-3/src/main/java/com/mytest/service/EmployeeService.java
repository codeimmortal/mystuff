package com.mytest.service;
import org.springframework.stereotype.Service;

import com.mytest.exception.EmployeeServiceException;
import com.mytest.model.Employee;
@Service
public class EmployeeService {

		public String getsearchdata() {
			return "This is data";
		}
		//return employee object
		public Employee getEmployee() throws EmployeeServiceException {
			Employee emp = new Employee();
			emp.setName("emp1");
			emp.setDesignation("manager");
			emp.setEmpId("1");
			emp.setSalary(3000);

			return emp;
		}
		
		public Employee getRunEx() {
			Float f = 1f/0f;
			return null;
		}

	    //return employee as null
		public Employee getEmployeeNull() throws EmployeeServiceException {

			return null;
		}

	    //throw exception
		public Employee getEmployeeException() throws EmployeeServiceException {

			throw new EmployeeServiceException();
		}

	}

