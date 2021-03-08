import ipaddress
import streamlit as st


IP_PLACEHOLDER = "XXX.XXX.XXX.XXX"
GATEWAY_PLACEHOLDER = "XXX.XXX.XXX.XXX"
MASK_PLACEHOLDER = "XXX.XXX.XXX.XXX"


def validation(ip: str, gateway: str, mask: str):
    try:
        ip_ = ipaddress.IPv4Address(ip)
        if ip_ not in ipaddress.IPv4Network(f"{gateway}/{mask}", False).hosts():
            st.header("Error: IP not in range")
        else:
            if not ip_.is_private:
                st.warning("Warning! This ip is not in a standard private range.")

            st.success("Valid")
            st.write("IP address:", ip)
            st.write("Mask:", mask)
            st.write("Gateway:", gateway)

    except Exception as e:
        st.error(e)
        st.stop()


st.title("IP validator")

ip = st.text_input("IP address", value=IP_PLACEHOLDER)
mask = st.text_input("Mask", value=GATEWAY_PLACEHOLDER)
gateway = st.text_input("Gateway", value=GATEWAY_PLACEHOLDER)

if st.button("Validate"):
    if ip == IP_PLACEHOLDER:
        st.error("Please fill an IP address")
    elif gateway == GATEWAY_PLACEHOLDER:
        st.error("Please fill a Gateway address")
    elif mask == MASK_PLACEHOLDER:
        st.error("Please fill a mask")
    elif ip == gateway:
        st.error("IP and Mask should be different!")
    else:
        validation(ip, gateway, mask)
