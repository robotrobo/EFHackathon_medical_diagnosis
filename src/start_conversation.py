import streamlit as st
from time import sleep
import random
from backend import prep_chain, get_final_analysis
import json
from testconvo import testConvo, chunk_string
def start_conversation(patient_info):
	chain = prep_chain()
	st.subheader('Conversation Transcript')
		 
	messages = chunk_string(testConvo)
	overall_analysis = []
	for message in messages:
			st.text(message)

			result = chain({"question": message, "chat_history": [], "patient_info": patient_info})
			print(result)
			chat_answer = result["answer"]
			
			try:
				parsed_output = json.loads(chat_answer)
				overall_analysis.append(parsed_output)
			except Exception as e:
				print(e)
				pass
			try:
				st.info("Diagnosis: " + parsed_output["diagnosis"], icon="🩺")
			except Exception as e:
				print(e)
			try:
				st.success("Possible treatments: "  + parsed_output["treatment"], icon="👨‍⚕️")
			except Exception as e:
				print(e)
			try:
				st.info("Ask the patient: " + parsed_output["next_question"], icon="🙋")
			except Exception as e:
				print(e)
			try:
				st.warning("notes: " + parsed_output["notes"], icon="📝")
			except Exception as e:
				print(e)
	st.divider()
	analysis = get_final_analysis(overall_analysis)
	st.subheader("Final Analysis")
	st.write(analysis)
