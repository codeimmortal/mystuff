package com.mytest.exception;

public class RecordNotFoundException extends Exception {

		private static final long serialVersionUID = -9079454849611061074L;

		public RecordNotFoundException() {
			super();
		}

		public RecordNotFoundException(final String message) {
			super(message);
		}

	}
