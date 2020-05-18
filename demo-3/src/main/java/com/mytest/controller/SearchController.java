package com.mytest.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import com.mytest.exception.EmployeeServiceException;
import com.mytest.exception.RecordNotFoundException;
import com.mytest.model.Employee;
import com.mytest.service.EmployeeService;

@RestController
public class SearchController {
	@Autowired
	EmployeeService employeeService;

    //Happy path, an employee is returned as response
	@RequestMapping(value = "/employee", method = RequestMethod.GET)
	public Employee getEmpl() throws RecordNotFoundException, EmployeeServiceException {
		try {
			Employee emp = employeeService.getEmployee();

			if (emp == null) {
				throw new RecordNotFoundException("Employee not found");
			}
			return emp;
		} catch (EmployeeServiceException e) {
			throw new EmployeeServiceException("Internal Server Exception while getting exception");
		}
	}

    //no employee found so RecordNotFoundException is thrown
	@RequestMapping(value = "/employee2", method = RequestMethod.GET)
	public Employee getEmp2() throws RecordNotFoundException, EmployeeServiceException {
		try {
			Employee emp = employeeService.getEmployeeNull();
			if (emp == null) {
				throw new RecordNotFoundException("Employee not found");
			}

			return emp;
		} catch (EmployeeServiceException e) {
			throw new EmployeeServiceException("Internal Server Exception while getting exception");
		}
	}

    //Some exception is thrown by service layer
	@RequestMapping(value = "/employee3", method = RequestMethod.GET)
	public Employee getEmp3() throws RecordNotFoundException, EmployeeServiceException {
		try {
			Employee emp = employeeService.getEmployeeException();
			if (emp == null) {
				throw new RecordNotFoundException("Employee not found");
			}
			return emp;
		} catch (EmployeeServiceException e) {
			throw new EmployeeServiceException("Internal Server Exception while getting exception");
		}
	}
	
	 //Some exception is thrown by service layer
		@RequestMapping(value = "/employee4", method = RequestMethod.GET)
		public Employee getRunEx() throws RecordNotFoundException, EmployeeServiceException, Exception {
			try {
				Float f = 1f/0f;
				Employee emp = employeeService.getRunEx();
				if (emp == null) {
					throw new RecordNotFoundException("Employee not found");
				}
				return emp;
			} catch (Exception e) {
				throw new Exception("Other exception");
			}
		}
}
